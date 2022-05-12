#from pyrogram import Client, Message
from pyrogram import Client
from pyrogram.types import Message
from pyrogram.handlers import MessageHandler
from pyrogram import  filters
from bot import LOCAL, CONFIG, STATUS
from bot.handlers import help_message_handler

async def func(client : Client, message: Message):
    try:
        await message.delete()
    except:
        pass
    if ' '.join(message.command[1:]) == CONFIG.BOT_PASSWORD:
        STATUS.CHAT_ID.append(message.chat.id)
        await help_message_handler.func(client, message)
