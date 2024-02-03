import discord
import os
import urllib.parse
import requests
import base64
import hashlib
import json
import time
import asyncio
import threading
import websocket
import subprocess
import socket
import random
import string
import pygui as gui
from cryptography.fernet import Fernet
from json import dumps
from winotify import Notification, audio
from datetime import datetime
from colorama import Fore
from pystyle import Colorate, Colors, Center, Box
from discord.ext import commands


with open('config.json', 'r') as config_file:
    config = json.load(config_file)

token = config.get('token')
prefix = config.get('prefix')

if not token:
    print("Please Provide Your Valid User Token In The config.json File.")
    print("Additionally, You Can Add A Custom Prefix In The config.json File")
    time.sleep(6.5)
    exit()

client = discord.Client()
bot = commands.Bot(command_prefix=prefix)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    print(f"""Thank You For Using Astro Selfbot.
             Type {prefix}help For A List Of Commands.
                    Made By Topher
          """)




@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(f"Invalid Command. Type '{prefix}help' For A List Of Valid Commands.")

@bot.command()
async def help(ctx):
    await ctx.send("""
        Astro Sb Help
    
""")



@bot.command()
async def spam(ctx, self, message: str, times: int):
  if times > 50:
    await ctx.send("Do Not Send More Than 50 Messages!")
  else:
    for x in range(times):
      await ctx.send(message)  
      print(f"Command Output | spam | Successfully Spammmed '{message}'.")

@bot.command()
async def purgehack(ctx, self, times: int):
  if times > 50:
    await ctx.send("Max Purge Times Is 50.")
  else:
    for x in range(times):
      await ctx.send(""".






















                     

























































































Lol It Was Pruged WHY CANT I SPELL PURGED GRR
""")  
      print(f"Command Output | purge | Successfully Purged {times} Times.")


client.run(token, bot=False)

@bot.command()
async def tokensniff(ctx, user: discord.User):
    await ctx.message.delete()
    token = base64.b64encode(str(user.id).encode('utf-8')).decode('utf-8').rstrip('=')
    info = f"""
>--------------------------------------------------<
               Token Sniff Results
First 29 Characters Of {user.name}'s Token: {token}
>--------------------------------------------------<
    """
    await ctx.send(f"{info}")
    print(f"Command Output | tokensniff | Sniffed {user.name}'s Token.")