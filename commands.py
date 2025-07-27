from telethon import events

def register_commands(client):
    @client.on(events.NewMessage(pattern=r'\.مرحبا'))
    async def greet(event):
        await event.respond("أهلا وسهلا، البوت شغّال! 🤖🔥")
import time
start_time = time.time()

from telethon import events
from telethon.tl.functions.contacts import BlockRequest, UnblockRequest
import os

def register_all_commands(client):

    # --------- أوامر أساسية ---------
    @client.on(events.NewMessage(pattern=r'\.فحص'))
async def cmd_check(event):
    current_time = time.time()
    uptime = int(current_time - start_time)
    hours = uptime // 3600
    minutes = (uptime % 3600) // 60
    seconds = uptime % 60

    await event.respond(
        f"🔍 **فحص النظام**\n\n"
        f"✅ البوت يعمل بكفاءة!\n"
        f"🕒 مدة التشغيل: {hours} ساعة و {minutes} دقيقة و {seconds} ثانية\n"
        f"📌 النسخة: v1.0\n"
        f"⚡ توقيع البوت: عمّار 💻🚀"
    )

    @client.on(events.NewMessage(pattern=r'\.حذف'))
    async def cmd_delete(event):
        await event.delete()

    @client.on(events.NewMessage(pattern=r'\.كرر (.*)'))
    async def cmd_repeat(event):
        try:
            parts = event.pattern_match.group(1).split(" ", 1)
            count = int(parts[0])
            text = parts[1]
            for _ in range(count):
                await event.respond(text)
        except:
            await event.respond("❌ الصيغة: .كرر <عدد> <النص>")

    @client.on(events.NewMessage(pattern=r'\.تحميل'))
    async def cmd_download(event):
        reply = await event.get_reply_message()
        if reply and reply.media:
            await event.respond("⏳ جاري التحميل...")
            path = await reply.download_media()
            await event.respond(f"✅ تم التحميل: {path}")
        else:
            await event.respond("❌ لازم ترد على ملف أو ميديا")

    @client.on(events.NewMessage(pattern=r'\.رفع (.*)'))
    async def cmd_upload(event):
        file_name = event.pattern_match.group(1)
        if os.path.exists(file_name):
            await event.respond("⏳ جاري الرفع...")
            await client.send_file(event.chat_id, file_name)
            await event.respond("✅ تم رفع الملف")
        else:
            await event.respond("❌ الملف غير موجود")

    # --------- أوامر إدارية ---------
    @client.on(events.NewMessage(pattern=r'\.حظر'))
    async def cmd_block(event):
        reply = await event.get_reply_message()
        if reply:
            await client(BlockRequest(reply.sender_id))
            await event.respond("🚫 تم الحظر")
        else:
            await event.respond("❌ لازم ترد على الشخص حتى تحظره")

    @client.on(events.NewMessage(pattern=r'\.فكحظر'))
    async def cmd_unblock(event):
        reply = await event.get_reply_message()
        if reply:
            await client(UnblockRequest(reply.sender_id))
            await event.respond("✅ تم فك الحظر")
        else:
            await event.respond("❌ لازم ترد على الشخص حتى تفك الحظر")

    @client.on(events.NewMessage(pattern=r'\.كتم'))
    async def cmd_mute(event):
        reply = await event.get_reply_message()
        if reply:
            await client.edit_permissions(event.chat_id, reply.sender_id, send_messages=False)
            await event.respond("🔇 تم كتم العضو")
        else:
            await event.respond("❌ لازم ترد على الشخص حتى تكتمه")

    @client.on(events.NewMessage(pattern=r'\.رفعكتم'))
    async def cmd_unmute(event):
        reply = await event.get_reply_message()
        if reply:
            await client.edit_permissions(event.chat_id, reply.sender_id, send_messages=True)
            await event.respond("🔊 تم رفع الكتم")
        else:
            await event.respond("❌ لازم ترد على الشخص حتى ترفع الكتم")

    @client.on(events.NewMessage(pattern=r'\.تثبيت'))
    async def cmd_pin(event):
        reply = await event.get_reply_message()
        if reply:
            await client.pin_message(event.chat_id, reply.id)
            await event.respond("📌 تم التثبيت")
        else:
            await event.respond("❌ لازم ترد على الرسالة حتى تثبتها")

    # --------- أوامر كروبات ---------
    @client.on(events.NewMessage(pattern=r'\.غادر'))
    async def cmd_leave(event):
        await event.respond("👋 جاري مغادرة الكروب ...")
        await client.delete_dialog(event.chat_id)

    @client.on(events.NewMessage(pattern=r'\.تنظيف (.*)'))
    async def cmd_purge(event):
        try:
            count = int(event.pattern_match.group(1))
            msgs = []
            async for msg in client.iter_messages(event.chat_id, limit=count + 1):
                msgs.append(msg.id)
            await client.delete_messages(event.chat_id, msgs)
            await event.respond(f"🗑️ تم حذف {count} رسالة")
        except:
            await event.respond("❌ الصيغة: .تنظيف <عدد>")
