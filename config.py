import os
import heroku3
from telethon import TelegramClient, events
#
# Buranı qurdalama
# Yalnız deploy buttonuyla botunu yarat
# 
api_id = int(os.environ.get("APP_ID", "19485442"))
api_hash = os.environ.get("API_HASH", "a03fcb372b3ec4e406b5d52f84b02e53")
bot_token = os.environ.get("TOKEN", "5394785524:AAGiGd4Xth_0Fa4oe32FYWEAfbTVbeD_W4M")
# Telethon 
client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)
#
USERNAME = os.environ.get("USERNAME")
log_qrup = int(os.environ.get("LOG_QRUP"))
startmesaj = os.environ.get("startmesaj")
komutlar = os.environ.get("komutlar")
qrupstart = os.environ.get("qrupstart")
support = os.environ.get("support")
sahib = os.environ.get("sahib")
#
# mutsuz_panda 
# mutsuz_panda 
# mutsuz_panda 
