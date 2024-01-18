from telethon import TelegramClient, events
import time
from dotenv import dotenv_values

config = dotenv_values(".env")
api_id, api_hash = config["api_id"], config["api_hash"]

client = TelegramClient("TeleAutoReply", api_id, api_hash).start()
message = "[Automatic Reply] Hi, I'm currently unavailable. Feel free to call if it's urgent."

@client.on(events.NewMessage())
async def _(event):
	if event.is_private:
		time.sleep(1)
		sender = await event.get_input_sender()
		await client.send_message(sender, message)

client.run_until_disconnected()