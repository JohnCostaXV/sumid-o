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

prefix = ["d.", "diane "]

client = commands.Bot(command_prefix=prefix, case_insensitive=True)
shared = discord.AutoShardedClient(shard_count=2, shard_ids=(1,2))
client.remove_command("help")


modulos = ["cogs.fun", "cogs.giveaway", "cogs.banco", "cogs.minecraft"]

@client.event
async def on_ready():
    print("=========================")
    print(f"Nome: {client.user.name}")
    print(f"ID: {client.user.id}")
    print("BOT: Online")
    print("=========================")


@client.event
async def on_guild_join(guild):
    url = "mongodb://admin:J123456@ds023428.mlab.com:23428/zephyr_bot"
    mongo = MongoClient(url)
    zephyr_bot = mongo["zephyr_bot"]
    servidores = zephyr_bot["servidores"]
    servidor = {
        "_ServidorID":str(guild.id),
        "ServidorNome":str(guild.name),
        "CanalBV":"nenhum",
        "OnBV":"não",
        "BVmsg":"Nenhum",
        "Tipomsg":"Nenhuma",
        "Modrole":"Nenhuma"
    }
    zephyr_bot.servidores.insert_one(servidor).inserted_id

    print(f"Servidor detectado: {guild.name}({guild.id}).")
    print("Já foi registrado no banco de dados!")

@client.event
async def on_guild_remove(guild):
    url = "mongodb://admin:J123456@ds023428.mlab.com:23428/zephyr_bot"
    mongo = MongoClient(url)
    zephyr_bot = mongo["zephyr_bot"]
    servidores = zephyr_bot["servidores"]
    zephyr_bot.servidores.delete_one({"_ServidorID":str(guild.id)})

    print(f"Acabei de sair do {guild.name}.")
    print("Todos dados foram deletados.")


@client.event
async def on_member_join(member):
        url = "mongodb://admin:J123456@ds023428.mlab.com:23428/zephyr_bot"
        mongo = MongoClient(url)
        zephyr_bot = mongo["zephyr_bot"]
        servidores = zephyr_bot["servidores"]
        banco = zephyr_bot.servidores.find_one({"_ServidorID":str(member.guild.id)})
        msg = banco["BVmsg"]
        canal = banco["CanalBV"]
        tipo = banco["Tipomsg"]


        if banco["Tipomsg"] == "1":
            url = requests.get(member.avatar_url)
            avatar = Image.open(BytesIO(url.content))
            avatar = avatar.resize((320, 320));
            bigsize = (avatar.size[0] * 3,  avatar.size[1] * 3)
            mask = Image.new('L', bigsize, 0)
            draw = ImageDraw.Draw(mask)
            draw.ellipse((0, 0) + bigsize, fill=255)
            mask = mask.resize(avatar.size, Image.ANTIALIAS)
            avatar.putalpha(mask)

            output = ImageOps.fit(avatar, mask.size, centering=(0.5, 0.5))
            output.putalpha(mask)
            output.save('avatar.png')

            #avatar = Image.open('avatar.png')
            fundo = Image.open('bemvindo.jpg')
            fonte = ImageFont.truetype('BebasNeue.ttf',70)
            fonte1 = ImageFont.truetype('BebasNeue.ttf', 100)
            escrever = ImageDraw.Draw(fundo)
            escrever.text(xy=(620,650), text="Bem-vindo", fill=(224, 235, 234), font=fonte1)
            escrever.text(xy=(700,750), text=member.name, fill=(224, 235, 234), font=fonte)
            fundo.paste(avatar, (620, 290), avatar)
            fundo.save('bv.png')

            await client.get_channel(canal).send(member.mention)
            await client.get_channel(canal).send(file=discord.File('bv.png'))
        
        elif banco["Tipomsg"] == "2":
            await client.get_channel(canal).send(msg.replace("{servidor_name.upper}",str(member.guild.name.upper())).replace("{membro_mention}",str(member.mention)).replace("{servidor_name}",str(member.guild.name)).replace("{servidor_id}",str(member.guild.id)).replace("{membro_id}",str(member.id)).replace("{membro_name}",str(member.name)))
        elif banco["Tipomsg"] == "3":
            return
        else:
            pass
    



if __name__ == "__main__":
 try:
   for modulo in modulos:
     client.load_extension(modulo)
 except Exception as error:
     print(f"[Erro] : {modulo} - {error}")


client.run()
