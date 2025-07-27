from telethon import events

@bot.on(events.NewMessage(pattern=r'^\.فحص$'))
async def system_check(event):
    await event.reply("✅ البوت شغّال بكل طاقته!\n🔧 توقيع: عمّار ⚡")
