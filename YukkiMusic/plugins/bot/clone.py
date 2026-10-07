import uuid

import config
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery

from YukkiMusic import app
from YukkiMusic.core.mongo import mongodb

clone_requests = mongodb.clone_requests
clone_registry = mongodb.clone_registry
CLONE_PRICE = 399

def _is_owner(user_id):
    return user_id in config.OWNER_ID

def _request_id():
    return uuid.uuid4().hex[:10].upper()

@app.on_message(filters.command("clone") & filters.private & ~filters.edited)
async def clone_start(client, message: Message):
    if not config.CLONE_QR_IMAGE:
        return await message.reply_text("❌ Clone payment is not open yet. The owner has not added the payment QR.")
    await message.reply_photo(
        config.CLONE_QR_IMAGE,
        caption=(
            "💠 CLONE BOT — ₹399\n\n"
            "1. Scan the QR and complete the payment.\n"
            "2. Take a clear payment screenshot.\n"
            "3. Reply to that screenshot with /clonepay TRANSACTION_ID\n\n"
            "⚠️ Payment is manually verified by the owner.\n"
            "Your clone is registered only after approval.\n\n"
            "🔐 Never send a BotFather token in this chat."
        ),
    )

@app.on_message(filters.command("clonepay") & filters.private & ~filters.edited)
async def clone_payment(client, message: Message):
    reply = message.reply_to_message
    if not reply or not (reply.photo or reply.document):
        return await message.reply_text("❌ Reply to your payment screenshot with /clonepay TRANSACTION_ID.")
    if len(message.command) != 2:
        return await message.reply_text("Usage: reply to the payment screenshot with /clonepay TRANSACTION_ID")
    reference = message.command[1].strip()
    if len(reference) < 3 or len(reference) > 100:
        return await message.reply_text("❌ Invalid transaction/reference ID.")
    request_id = _request_id()
    existing = await clone_requests.find_one({"user_id": message.from_user.id, "status": "pending"})
    if existing:
        return await message.reply_text(f"⏳ You already have a pending clone request: {existing['request_id']}")
    data = {"request_id": request_id, "user_id": message.from_user.id, "username": message.from_user.username, "reference": reference, "status": "pending"}
    await clone_requests.insert_one(data)
    try:
        forwarded = await reply.copy(config.LOG_GROUP_ID)
        await forwarded.reply_text(
            f"💳 CLONE PAYMENT REQUEST\n\nRequest: {request_id}\nUser ID: {message.from_user.id}\nUsername: @{message.from_user.username or 'N/A'}\nReference: {reference}\nAmount: ₹{CLONE_PRICE}\n\nVerify the payment before approving.",
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("✅ APPROVE", callback_data=f"clone_approve:{request_id}"),
                InlineKeyboardButton("❌ REJECT", callback_data=f"clone_reject:{request_id}"),
            ]]),
        )
    except Exception:
        await clone_requests.delete_one({"request_id": request_id})
        return await message.reply_text("❌ Could not send the request to the owner/log group. Please try again.")
    await message.reply_text(f"✅ Payment proof submitted.\n\nRequest ID: {request_id}\n⏳ Wait for manual owner verification.")

@app.on_callback_query(filters.regex(r"^clone_(approve|reject):"))
async def clone_review(client, callback: CallbackQuery):
    if not _is_owner(callback.from_user.id):
        return await callback.answer("Owner only.", show_alert=True)
    request_id = callback.data.split(":", 1)[1]
    request = await clone_requests.find_one({"request_id": request_id})
    if not request:
        return await callback.answer("Request not found.", show_alert=True)
    action = callback.data.split(":", 1)[0].replace("clone_", "")
    if request.get("status") != "pending":
        return await callback.answer(f"Already {request.get('status')}.", show_alert=True)
    status = "approved" if action == "approve" else "rejected"
    await clone_requests.update_one({"request_id": request_id}, {"$set": {"status": status, "reviewed_by": callback.from_user.id}})
    if status == "approved":
        await clone_registry.update_one({"user_id": request["user_id"]}, {"$set": {"user_id": request["user_id"], "request_id": request_id, "status": "approved"}}, upsert=True)
        text = f"✅ Approved\n\nRequest {request_id} approved.\nClone registration is recorded; runtime activation requires a separate bot process/token setup."
    else:
        text = f"❌ Rejected\n\nRequest {request_id} rejected."
    try:
        await callback.message.edit_text(text)
    except Exception:
        pass
    try:
        await app.send_message(request["user_id"], "🎉 Your clone request was approved." if status == "approved" else "❌ Your clone request was rejected.")
    except Exception:
        pass
    await callback.answer(status.title())

@app.on_message(filters.command("myclones") & filters.private & ~filters.edited)
async def my_clones(client, message: Message):
    rows = await clone_registry.find({"user_id": message.from_user.id}).to_list(length=20)
    if not rows:
        return await message.reply_text("📭 You have no approved clone registrations.")
    lines = ["🤖 YOUR CLONES", ""]
    for row in rows:
        lines.append(f"• {row.get('request_id', 'N/A')} — {row.get('status', 'unknown')}")
    await message.reply_text("\n".join(lines))

@app.on_message(filters.command("cloneinfo") & filters.private & ~filters.edited)
async def clone_info(client, message: Message):
    if not _is_owner(message.from_user.id):
        return
    pending = await clone_requests.count_documents({"status": "pending"})
    approved = await clone_requests.count_documents({"status": "approved"})
    await message.reply_text(f"🔐 CLONE STATUS\n\n⏳ Pending: {pending}\n✅ Approved: {approved}\n💰 Price: ₹{CLONE_PRICE}")
