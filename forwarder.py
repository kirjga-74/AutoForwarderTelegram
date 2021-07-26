from telethon import TelegramClient, events
import os
cwd = os.getcwd()
"""GANTI DATA DIBAWAH INI DENGAN DATA ANDA"""
api_id = 1234567 #API ID user
api_hash = "9fa988f11135f1c5b3178841112850a7" #api hash user
client = TelegramClient('anon', api_id, api_hash)
client.start()
# CHAT_ID_A = -417043978 #chat ID SUMBER 
# CHAT_ID_B = -599761503 #chat ID tujuan
file_lists = "data.txt"
myfiles = open(f"{cwd}/{file_lists}","r")
list_accounts = myfiles.read()
get_data = list_accounts.split("|")
CHAT_ID_A = get_data[0]
CHAT_ID_B = get_data[1]
@client.on(events.NewMessage(chats=CHAT_ID_A))
async def handle_new_message(event):
    await client.forward_messages(CHAT_ID_B, event.message)
    
with client:
    client.run_until_disconnected()
