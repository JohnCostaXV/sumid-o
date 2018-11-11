import discord
from discord.ext import commands
import requests
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont, ImageOps
import json
from pymongo import MongoClient
import pymongo 
import random
import asyncio
import time
import os

prefix = ["d."]

client = commands.Bot(command_prefix=prefix, case_insensitive=True)
shared = discord.AutoShardedClient(shard_count=2, shard_ids=(1,2))
client.remove_command("help")



@client.event
async def on_ready():
    print("BOT ONLINE")

@client.event
async def on_message(message):
    if message.content.lower().startswith("d.suafoto"):
        user = message.mentions[0]
        if user is None:
            url = requests.get(message.author.avatar_url)
            avatar = Image.open(BytesIO(url.content))
            #                  largura x altura
            avatar = avatar.resize((325, 375));
            avatar.save('suafoto.png')

            fundo = Image.open('fototua.png')
            fundo.paste(avatar, (210, 90))
            fundo.save('suafoto.png')

            await message.channel.send(file=discord.File('suafoto.png'))
        else:
            url = requests.get(user.avatar_url)
            avatar = Image.open(BytesIO(url.content))
            #                  largura x altura
            avatar = avatar.resize((325, 375));
            avatar.save('suafoto.png')

            fundo = Image.open('fototua.png')
            fundo.paste(avatar, (210, 90))
            fundo.save('suafoto.png')

            await message.channel.send(file=discord.File('suafoto.png'))
    
    
    if message.content.lower().startswith("d.ship"):
        try:

            url1 = requests.get(message.mentions[0].avatar_url)
            url2 = requests.get(message.mentions[1].avatar_url)
            ship_img = requests.get('https://cdn.discordapp.com/attachments/425866183904854029/488105962734092289/ship_img.png')
            avatar1 = Image.open(BytesIO(url1.content))
            avatar2 = Image.open(BytesIO(url2.content))
            avatar1 = avatar1.resize((400, 400), Image.ANTIALIAS);
            avatar2 = avatar2.resize((400, 400), Image.ANTIALIAS);
            ship = Image.open(BytesIO(ship_img.content))
            ship.paste(avatar1, (0, 0))
            ship.paste(avatar2, (800, 0))
            ship.save('ship.png')
            cont = message.mentions[0].name
            cont2 = message.mentions[1].name
            cont3 = len(cont2)
            cont4 = cont3 - 4
            cont5 = cont[0:4]
            cont6 = cont2[cont4:cont3]
            cont7 = cont5 + cont6
            chance = random.randint(10,100)
            await message.channel.send(f"Esse canal tem **{chance}%** de chance de dar certo!\n\n**{cont7}**")
            await message.channel.send(file=discord.File('ship.png'))
        except IndexError:
            await message.channel.send(f"**{message.author.name}**, você precisa **mencionar dois usuários** diferentes.")
    

    if message.content.lower().startswith("d.clone"):
        try:
            pfp = requests.get(message.author.avatar_url_as(format='png', size=256)).content
            hook = await message.channel.create_webhook(name=message.author.display_name, avatar=pfp)
            await hook.send(message)
            await hook.delete()
        except discord.errors.Forbidden:
            await message.channel.send(f"❌ | **{message.author.name}**, estou **sem permissão** de `GERENCIAR WEBHOOKS`.")



client.run(os.environ.get("token"))
