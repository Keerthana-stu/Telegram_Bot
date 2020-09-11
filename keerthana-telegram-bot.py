!pip install adafruit-io
import os

Adafruit_User = os.getenv(Adafruit_User)
Adafruit_IO_Key= os.getenv(Adafruit_IO_Key)

from Adafruit_IO import Client, Feed
aio = Client(Adafruit_User,Adafruit_IO_Key)

feed = Feed(name='bot')

!pip install python-telegram-bot

from Adafruit_IO import Data

from telegram.ext import Updater,CommandHandler
import requests
def automationOn(bot,update):
  from_user = 'Turning On'
  chat_id = update.message.chat_id
  bot.send_message(chat_id,from_user)
  value = Data(value=1)
  value_send = aio.create_data('bot',value)

def automationOff(bot,update):
  from_user = 'Turning Off'
  chat_id = update.message.chat_id
  bot.send_message(chat_id,from_user)
  value = Data(value=0)
  value_send = aio.create_data('bot',value)

u = Updater(os.getenv(Key))
dp = u.dispatcher
dp.add_handler(CommandHandler('On',automationOn))
dp.add_handler(CommandHandler('Off',automationOff))
u.start_polling()
u.idle()
  
