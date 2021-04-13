from telethon import events
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import ImportChatInviteRequest
global sources

client = TelegramClient('anon', 715737, "e2e6e706ff438f58cf6f42c894063ed1")

@client.on(events.NewMessage)
async def my_event_handler(event):
    global sources
    chat = await event.get_chat()
    sender = await event.get_sender()
    chat_id = event.chat_id
    sender_id = event.sender_id
    #if str(chat.id)=="1444042095":
    if str(chat.id) in sources.keys():
        #await client.send_message(1249866283, event.message)
        await client.reply_to_message(int(sources[str(chat.id)]), event.message)


data=open("sources.txt","r").read().split("\n")
while "" in data:data.remove("")
sources = {source.split(":")[0]:source.split(":")[1] for source in data}

client.start()
client.run_until_disconnected()
