from telethon import events
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import ImportChatInviteRequest
client = TelegramClient('anon', 715737, "e2e6e706ff438f58cf6f42c894063ed1")

@client.on(events.NewMessage)
async def my_event_handler(event):
    chat = await event.get_chat()
    sender = await event.get_sender()
    chat_id = event.chat_id
    sender_id = event.sender_id
    print (chat.id)
    #print (sender)
    print (chat_id)
    #print (sender_id)
    print (event.media)
    #destination_user_username='Destination'
    #entity=await client.get_entity("Destination")
    #updates = await client(ImportChatInviteRequest('AAAAAFUe_UyK1izc5Hu86Q'))
    if str(chat.id)=="1067356457":
        #await client.send_message(1249866283,event.raw_text)
        await client.send_message(1363606222, event.message)

client.start()
client.run_until_disconnected()
