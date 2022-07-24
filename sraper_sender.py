
import telebot
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser, InputPeerChannel
from telethon import TelegramClient, sync, events
 


api_id = '15953907'
api_hash = 'cb4a2f78514e8c767fdcf139069bb3f1'
token = '5377807583:AAEspcFJ2nezWCLHTxrVfC7RHv8LGOb0RPo'
message = "WASPADA, Ada Paket Terindikasi Serangan DDoS!!!"
 

phone = '+6285348185165'


client = TelegramClient('session', api_id, api_hash)

client.connect()
 

if not client.is_user_authorized():
  
    client.send_code_request(phone)
     

    client.sign_in(phone, input('Enter the code: '))
  
try:
   
    receiver = InputPeerUser(1370329552, 0)
 

    client.send_message(receiver, message, parse_mode='html')
except Exception as e:
     
    print(e);
 
client.disconnect()


