#from pyrogram import Client, Message, Filters
from pyrogram import Client
from pyrogram.types import Message
from pyrogram.handlers import MessageHandler
from pyrogram import  filters
from bot import COMMAND
from bot.handlers import leech_handler

@Client.on_message(Filters.private & ~Filters.regex(r'^/'))
async def func(client : Client, message : Message):
    message.text = "/" + COMMAND.LEECH + " " + message.text
    return await leech_handler.func(client, message)