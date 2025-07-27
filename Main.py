from telethon import TelegramClient
from commands import register_commands  # تأكد أن ملفك بنفس الاسم

client = TelegramClient('session', api_id, api_hash)

register_commands(client)  # هنا نربط الأوامر بالبوت

client.start()
client.run_until_disconnected() 
from telethon import TelegramClient, events
import config
import commands

if not all([config.API_ID, config.API_HASH, config.SESSION]):
    print("❌ تأكد من إضافة API_ID, API_HASH, SESSION في Render")
    exit()

client = TelegramClient(StringSession(config.SESSION), config.API_ID, config.API_HASH)

commands.register_all_commands(client)

print("✅ البوت بدأ العمل ...")
client.run_until_disconnected 
