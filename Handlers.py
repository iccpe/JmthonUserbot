from telethon import events
import time

# بدء التوقيت لحساب uptime
start_time = time.time()

@bot.on(events.NewMessage(pattern=r'^\.فحص$'))
async def system_check(event):
    current_time = time.time()
    uptime = int(current_time - start_time)
    hours = uptime // 3600
    minutes = (uptime % 3600) // 60
    seconds = uptime % 60

    await event.reply(
        f"🔍 **فحص النظام**\n\n"
        f"✅ البوت يعمل بكفاءة!\n"
        f"🕒 مدة التشغيل: {hours} ساعة و {minutes} دقيقة و {seconds} ثانية\n"
        f"📌 النسخة: v1.0\n"
        f"⚡ توقيع البوت: عمّار 💻🚀"
    )
