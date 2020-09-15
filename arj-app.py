from telegram.ext import Updater,CommandHandler
from Adafruit_IO import Data, Client, Feed
import os

Adafruit_IO_Name = os.getenv('Adafruit_IO_Name')
Adafruit_IO_Key = os.getenv('Adafruit_IO_key')
TOKEN = os.getenv('TOKEN')#Telegram BOT Token
aio = Client( Adafruit_IO_Name,Adafruit_IO_Key)
print("Client Created")
                              #Section 1 - Sending Value
#Commands for Turning ON 
def ON(bot,update):
  chat_id = update.message.chat_id                             
  bot.send_message(chat_id,text = "ON")
  bot.send_photo(chat_id,photo = 'https://www.securityroundtable.org/wp-content/uploads/2019/03/AdobeStock_261504199-300x169.jpeg')
  feed_value(1)

#Commands for Turning OFF
def OFF(bot,update):
  chat_id = update.message.chat_id                             
  bot.send_message(chat_id,text = "OFF")
  bot.send_photo(chat_id,photo = 'https://motionarray.imgix.net/preview-366781-SucOpqoSyhMdoEq8-large.jpg?w=1400&q=60&fit=max&auto=format')
  feed_value(0)
  

def feed_value(value):
  feeds = aio.feeds('light-control')
  aio.send_data(feeds.key,value) 
  
#Command to be executed when Bot starts
def start(bot,update):
  chat_id = update.message.chat_id
  start_message = "/ON TO TURN ON LIGHT    /OFF TO TURN OFF LIGHT"
  bot.send_message(chat_id,text = start_message)
  
u = Updater(TOKEN)#Updater is a library from telegram package( Authenticates the key)
dp = u.dispatcher
dp.add_handler(CommandHandler('ON',ON))
dp.add_handler(CommandHandler('OFF',OFF))
dp.add_handler(CommandHandler('start',start))
u.start_polling()
u.idle()
