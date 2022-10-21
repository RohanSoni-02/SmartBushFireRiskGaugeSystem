#!/usr/bin/env python3
from telegram import Bot
import serial

device = '/dev/ttyS0'

ser = serial.Serial(device, 9600)

chat_id = "-795551067"

with open("/home/pi/.local/share/.telegram_bot_token", "r") as f:
    telegram_token = f.read().rstrip()
    
bot = Bot(token=telegram_token)
print("send alert to user")
if(int(ser.readline()) > 30):
    bot.send_message(chat_id = chat_id, text="Alert fire was started. Water Motor is on!")
    
    