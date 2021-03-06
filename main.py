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
import datetime

palavra = ["a", "b", "c"]

forms = []
prefix = ["d."]
cor = 0x32363C
client = commands.Bot(command_prefix=prefix, case_insensitive=True)
shared = discord.AutoShardedClient(shard_count=2, shard_ids=(1,2))
client.remove_command("help")

@client.event
async def on_ready():
    print("BOT ONLINE")
    while True:
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{str(len(set(client.get_all_members())))} seres humanos!"))
        await asyncio.sleep(300)
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{str(len(set(client.guilds)))} servidores!"))
        await asyncio.sleep(300)

@client.event
async def on_message(message):

    if message.content.lower().startswith("d.invite"):
        await message.channel.send(f"{message.author.mention}, me adicione em seu servidor!\n- https://discordapp.com/oauth2/authorize?client_id=497012433378869250&permissions=8&scope=bot", delete_after=60)

    if message.content.lower().startswith("d.webabraçar"):
        try:
            membro = message.mentions[0]
            if message.author == membro:
                abraço = "https://akns-images.eonline.com/eol_images/Entire_Site/201398/rs_500x242-131008045420-justin-bieber-gifs1.gif"
                embed = discord.Embed(
                    color=cor
                )
                embed.set_image(url=abraço)
                await message.channel.send(f"{message.author.mention} talvez um abraço a si mesmo seja bom, as vezes.",embed=embed)
                return
            abraços = ["https://media1.tenor.com/images/3c83525781dc1732171d414077114bc8/tenor.gif?itemid=7830142", "https://media1.tenor.com/images/1069921ddcf38ff722125c8f65401c28/tenor.gif?itemid=11074788", "https://media1.tenor.com/images/7db5f172665f5a64c1a5ebe0fd4cfec8/tenor.gif?itemid=9200935", "http://media1.tenor.com/images/d7529f6003b20f3b21f1c992dffb8617/tenor.gif?itemid=4782499", "http://media1.tenor.com/images/11889c4c994c0634cfcedc8adba9dd6c/tenor.gif?itemid=5634578", "http://media1.tenor.com/images/949d3eb3f689fea42258a88fa171d4fc/tenor.gif?itemid=4900166", "http://media1.tenor.com/images/e58eb2794ff1a12315665c28d5bc3f5e/tenor.gif?itemid=10195705"]
            custom = random.choice(abraços)

            embed = discord.Embed(
                color=cor
            )
            embed.set_image(url=custom)
            await message.channel.send(f"{message.author.mention} web-abraçou {membro.name}", embed=embed)
        except IndexError:
            abraço = "https://akns-images.eonline.com/eol_images/Entire_Site/201398/rs_500x242-131008045420-justin-bieber-gifs1.gif"
            embed = discord.Embed(
                color=cor
            )
            embed.set_image(url=abraço)
            await message.channel.send(f"{message.author.mention} talvez um abraço a si mesmo seja bom, as vezes.",embed=embed)
            return
            


    if message.content.lower().startswith("d.cor"):
        msg = message.content.split(" ")
        inputcolor = " ".join(msg[1:])
        if inputcolor == '':
            randgb = lambda: random.randint(0, 255)
            hexcode = '%02X%02X%02X' % (randgb(), randgb(), randgb())
            rgbcode = str(tuple(int(hexcode[i:i+2], 16) for i in (0, 2, 4)))
            await message.channel.send('`Hexadecimal: #' + hexcode + '`\n`RGB: ' + rgbcode + '`')
            heximg = Image.new("RGB", (64, 64), '#' + hexcode)
            heximg.save("color.png")
            await message.channel.send(file=discord.File('color.png'))
        else:
            if inputcolor.startswith('#'):
                hexcode = inputcolor[1:]
                if len(hexcode) == 8:
                    hexcode = hexcode[:-2]
                elif len(hexcode) != 6:
                    await message.channel.send('Verifique se o código hexadecimal é este formato: `#7289DA`')
                rgbcode = str(tuple(int(hexcode[i:i+2], 16) for i in (0, 2, 4)))
                await message.channel.send('`Hexadecimal: #' + hexcode + '`\n`RGB: ' + rgbcode + '`')
                heximg = Image.new("RGB", (64, 64), '#' + hexcode)
                heximg.save("color.png")
                await message.channel.send(file=discord.File('color.png'))
            else:
                await message.channel.send('Verifique se o código hexadecimal é este formato: `#7289DA`')


    if message.content.lower().startswith("d.procurado"):
        try:
            usuario = message.mentions[0]    
            url = requests.get(usuario.avatar_url)
            img = requests.get('https://1.bp.blogspot.com/-Pup2Y3OdLog/WqLXBmgZ_1I/AAAAAAABAAw/BbTsnEIo7-0fDCSI6dtLzXxZXVBkgZg_QCLcBGAs/s1600/procura-se1.png')
            fundo = Image.open(BytesIO(img.content))
            avatar = Image.open(BytesIO(url.content))
                                #largura x altura
            avatar = avatar.resize((970, 1100));
            avatar.save('procurado.png')

            fundo.paste(avatar, (118, 260))
            fundo.save('procurado.png')

            await message.channel.send(content=message.author.mention, file=discord.File('procurado.png'))
        except IndexError:
            url = requests.get(message.author.avatar_url)
            img = requests.get('https://1.bp.blogspot.com/-Pup2Y3OdLog/WqLXBmgZ_1I/AAAAAAABAAw/BbTsnEIo7-0fDCSI6dtLzXxZXVBkgZg_QCLcBGAs/s1600/procura-se1.png')
            fundo = Image.open(BytesIO(img.content))
            avatar = Image.open(BytesIO(url.content))
                                #largura x altura
            avatar = avatar.resize((970, 1100));
            avatar.save('procurado.png')

            fundo.paste(avatar, (118, 260))
            fundo.save('procurado.png')


            await message.channel.send(content=message.author.mention, file=discord.File('procurado.png'))


    if message.content.lower().startswith("d.suafoto"):
        url = requests.get(message.author.avatar_url)
        url1 = requests.get('https://i.imgur.com/VlvM1Au.png')
        fundo = Image.open(BytesIO(url1.content))
        avatar = Image.open(BytesIO(url.content))
        avatar = avatar.resize((325, 375));
        avatar.save('suafoto.png')    

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
            await message.channel.send(f"Esse __casal__ tem **{chance}%** de chance de dar certo!\n\n**{cont7}**")
            await message.channel.send(file=discord.File('ship.png'))
        except IndexError:
            await message.channel.send(f"**{message.author.name}**, você precisa **mencionar dois usuários** diferentes.")
    

    if message.content.lower().startswith("d.clone"):
        try:
            msg = message.content.split(" ")
            msg1 = " ".join(msg[1:])
            pfp = requests.get(message.author.avatar_url_as(format='png', size=256)).content
            hook = await message.channel.create_webhook(name=message.author.display_name, avatar=pfp)
            await hook.send(msg1)
            await hook.delete()
        except discord.errors.Forbidden:
            await message.channel.send(f"❌ | **{message.author.name}**, estou **sem permissão** de `GERENCIAR WEBHOOKS`.")

    if message.content.lower().startswith("d.vercep"):
        args = message.content.split(" ")
        cep = " ".join(args[1:])
        url = requests.get("https://viacep.com.br/ws/"+cep+"/json/").json()
        cep = url['cep']
        rua = url['logradouro']
        bairro = url['bairro']
        cidade = url['localidade']
        estado = url['uf']

        embed = discord.Embed(
            title="Endereços por CEP",
            color=cor,
            description="**Informações:**\n\n"
                        "**Rua**: "+rua+"\n"
                        "**Bairro**: "+bairro+"\n"
                        "**Cidade**: "+cidade+"\n"
                        "**Estado**: "+estado+"\n"
        )
        await message.channel.send(content=message.author.mention,embed=embed)


    if message.content.lower().startswith("d.addbot"):
        try:
            if not message.guild.id == 498011182620475412:
                return
            else:
                server = message.channel
                new = client.get_guild(498011182620475412)
                if message.author not in new.members:
                    return await message.channel.send(f"<:incorreto:510894050103263245> **| {message.author.name}**, você precisa ser membro do servidor **`New Dev's`** para cadastrar seu bot.\n**CONVITE:** `https://discord.me/NewDevs`")
                if message.author.id in forms:
                    return await message.channel.send(f"<:incorreto:510894050103263245> **| {message.author.name}**, ainda existe um formulário sendo executado em seu privado.", delete_after=30)

                if message.author.bot:
                    return await message.channel.send("<:incorreto:510894050103263245> **|** BOTs não tem podem executar este comando!")

                author = message.author
                await message.channel.send(f"**{message.author.name}**, verifique sua mensagens diretas.")
                
                

                msg = await author.send("<:parceiro:510894109758586901> **|** **Então você quer adicionar o seu bot em nosso servidor?**\nPara isso precisamos que você preencha um pequeno formulário para cadastramento de seu BOT em nosso sistema e discord.\n\n<:bot:437248340724416514> **|** **Insira o `ID` do bot que deseja adicionar:** `2 minutos`")
                forms.append(message.author.id)
                try:
                        def check(m):
                            return m.author == message.author and m.channel.id == msg.channel.id
                        try:
                            idbot = await client.wait_for('message', check=check, timeout=120)
                        
                        except asyncio.TimeoutError:
                            await msg.delete()  

                        else:
                            if idbot.content == idbot.content:
                                await msg.delete()
                                try:
                                    usuario = await client.get_user_info(int(str(idbot.content)))
                                except:
                                    forms.remove(message.author.id)
                                    await author.send(f"<:incorreto:510894050103263245> | **{message.author.name}**, você pode apenas digitar um `ID` de um bot válido.")
                                else:
                                    if usuario in message.guild.members:
                                        forms.remove(message.author.id)
                                        ex = await author.send(f"<:incorreto:510894050103263245> **| {message.author.name}**, o `ID` fornecido pertence ao bot `{usuario}` no qual **ELE NÃO É SEU**. ")
                                        
                                        await asyncio.sleep(20)
                                        await ex.delete()
                                    else:

                                        if usuario.bot == False:
                                            forms.remove(message.author.id)
                                            erro = await author.send(f"<:incorreto:510894050103263245> **|** **{message.author.name}**, o `ID` que você forneceu **não corresponde** a de um **BOT** e por isso a **ação** foi **cancelada**.")
                                            
                                            await asyncio.sleep(20)
                                            await erro.delete()
                                            return
                                            
                                        elif usuario.bot == True:
                                            p = await author.send("<:Clyde:510894094877327360> **|** **Diga-nos agora o prefixo do seu BOT:** `2 minutos` `(máximo 8 caracteres)`")
                                            def check(m):
                                                return m.author == message.author and m.channel.id == p.channel.id

                                            try:
                                                prefix = await client.wait_for('message', check=check, timeout=120)
                                                await p.delete()
                                            
                                            except asyncio.TimeoutError:
                                                forms.remove(message.author.id)
                                                await p.delete()

                                            else:
                                                if prefix.content == prefix.content:
                                                    if len(prefix.content) +1 >= 8:
                                                        forms.remove(message.author.id)
                                                        error = await author.send(f"<:incorreto:510894050103263245> **|** **{message.author.name}**, o **prefixo** que você **forneceu execedeu** o **limite máximo**`(8)` e por isso a **ação** foi **cancelada**.")
                                                                
                                                        await asyncio.sleep(20)
                                                        await error.delete()
                                                    
                                                    else:
                                                        b = await author.send("<:DiscordDev:507925579245551616> **|** **Diga-nos agora a biblioteca que foi usada para desenvolver seu BOT:** `2 minutos`\n`Por exemplo: Discord.py, Discord.js, Eris, DiscordGo, Discord.Net, JDA, Discord-rs, Outros.`")
                                                        def check(m):
                                                            return m.author == message.author and m.channel.id == b.channel.id

                                                        try:
                                                            lang = await client.wait_for('message', check=check, timeout=120)
                                                            await b.delete()
                                                        except asyncio.TimeoutError:
                                                            forms.remove(message.author.id)
                                                            await b.delete()
                                                        else:
                                                            if lang.content == "Outros":
                                                                out1 = await author.send("<:DiscordDev:507925579245551616> **|** **Diga-nos o nome da biblioteca que você usou no desenvolvimento de seu BOT:** `2 minutos`")
                                                                def check(m):
                                                                    return m.author == message.author and m.channel.id == out1.channel.id
                                                                try:
                                                                    out = await client.wait_for('message', check=check, timeout=120)
                                                                    await out1.delete()
                                                                except asyncio.TimeoutError:
                                                                    await out1.delete()
                                                                else:
                                                                    if out.content == out.content:
                                                                        await author.send(f"<:correto:510894022861127680> | **{message.author.name}**, você completou todo **processo** para **adicionar** o bot `{usuario}` em **nosso servidor**.\n**OBS:** O formulário passará para um supervisor para avaliação.")
                                                                        
                                                                        logs = client.get_channel(507498277097177098)
                                                                        await logs.send(f"<:correto:510894022861127680> | {message.author.mention} **enviou** o bot `{usuario}` para ser **adicionado** em **nosso servidor**.")
                                                                
                                                                        pendenteEm = discord.Embed(
                                                                            colour=cor,
                                                                            description=f"**[TIPO]**: `Solicitação ADDBOT`\u200b",
                                                                            timestamp = datetime.datetime.utcnow()
                                                                        ).set_author(
                                                                            name=str(usuario),
                                                                            icon_url=usuario.avatar_url
                                                                        ).set_footer(
                                                                            text=f"ID: {usuario.id}"
                                                                        ).set_thumbnail(
                                                                            url=usuario.avatar_url
                                                                        ).add_field(
                                                                            name='📆 `| Criado em`',
                                                                            value=usuario.created_at.strftime('%d/%m/%y (%H:%M)')
                                                                        ).add_field(
                                                                            name="<:DiscordDev:507925579245551616> `| Biblioteca`",
                                                                            value=out.content
                                                                        ).add_field(
                                                                            name='<:parceiro:510894109758586901> `| Criador`',
                                                                            value=f"**{message.author}**\n`{message.author.id}`"
                                                                        ).add_field(
                                                                            name='<:Clyde:510894094877327360> `| Prefixo`',
                                                                            value=prefix.content
                                                                        ).add_field(
                                                                            name='📋 `| Descrição`',
                                                                            value="```Nenhuma```"
                                                                        ).add_field(
                                                                            name='🚀 `| Convite`',
                                                                            value=f"[link](https://discordapp.com/oauth2/authorize?client_id={usuario.id}&scope=bot&permissions=)"
                                                                        )
                                                                        forms.remove(message.author.id)
                                                                        
                                                                        msg = await client.get_channel(507570211499671576).send(embed=pendenteEm)                              
                                                                        await msg.add_reaction(":correto:515523764297924618")
                                                                        await msg.add_reaction(":incorreto:515523818358571039")
                                                                        

                                                                        def opt_check(reaction, user):
                                                                            return reaction.message.id == msg.id and str(reaction.emoji) in ['<:correto:515523764297924618>', '<:incorreto:515523818358571039>'] 
                                                                            
                                                                        try:
                                                                            reaction, user = await client.wait_for("reaction_add", check=opt_check, timeout=172800)
                                                                        
                                                                        except asyncio.TimeoutError:
                                                                            await author.send(f"Olá **{author.name}**, o seu bot `{usuario}` foi automaticamente rejeitado devido se passarem **2 dias** sem resposta, reenvie novamente.")
                                                                            await msg.clear_reactions()
                                                                        
                                                                        else:
                                                                            if str(reaction.emoji) == '<:correto:515523764297924618>':
                                                                                await msg.delete()
                                                                                await logs.send(f"<:correto:510894022861127680> | {message.author.mention}, seu bot `{usuario}` foi **aceito** pelo **{user.name}**.")
                                                                                await author.send(f"<:correto:510894022861127680> | O seu bot `{usuario}` foi **aceito** pelo **{user.name}**;")

                                                                            elif str(reaction.emoji) == '<:incorreto:515523818358571039>':
                                                                                mtv1 = await client.get_channel(507570211499671576).send(f"**{user.name}**, diga o **motivo** para **recusar** o bot `{usuario}`: `(2 minutos)`")
                                                                                
                                                                                def check(m):
                                                                                    return m.author == user and m.channel.id == mtv1.channel.id
                                                                                    
                                                                                try:
                                                                                    mtv = await client.wait_for('message', check=check, timeout=120)
                                                                                
                                                                                except asyncio.TimeoutError:
                                                                                    await mtv1.delete()
                                                                                    await msg.delete()
                                                                                    await logs.send(f"<:incorreto:510894050103263245> | {message.author.mention}, seu bot `{usuario}` foi **recusado** pelo **{user.name}**.\nMotivo:```Nenhum motivo informado```")
                                                                                    await author.send(f"<:incorreto:510894050103263245> | O seu bot `{usuario}` foi **recusado** pelo **{user.name}**.\nMotivo:```Nenhum motivo informado```")

                                                                                else:

                                                                                    if mtv.content == mtv.content:
                                                                                        await mtv1.delete()
                                                                                        await msg.delete()
                                                                                        await logs.send(f"<:incorreto:510894050103263245> | {message.author.mention}, seu bot `{usuario}` foi **recusado** pelo **{user.name}**.\nMotivo:```{mtv.content}```")
                                                                                        await author.send(f"<:incorreto:510894050103263245> | O seu bot `{usuario}` foi **recusado** pelo **{user.name}**.\nMotivo:```{mtv.content}```")
                                                                                        return
                                                                        
                                                            elif lang.content == lang.content:
                                                                await author.send(f"<:correto:510894022861127680> **|** **{message.author.name}**, você completou todo **processo** para **adicionar** o bot `{usuario}` em **nosso servidor**.\n**OBS:** O formulário passará para um supervisor para avaliação.")

                                                                logs = client.get_channel(507498277097177098)
                                                                await logs.send(f"<:correto:510894022861127680> | {message.author.mention} **enviou** o bot `{usuario}` para ser **adicionado** em **nosso servidor**.")

                                                                pendenteEm = discord.Embed(
                                                                    colour=cor,
                                                                    description=f"**[TIPO]**: `Solicitação BOT`\u200b",
                                                                    timestamp = datetime.datetime.utcnow()
                                                                ).set_author(
                                                                    name=str(usuario),
                                                                    icon_url=usuario.avatar_url
                                                                ).set_footer(
                                                                    text=f"ID: {usuario.id}"
                                                                ).set_thumbnail(
                                                                    url=usuario.avatar_url
                                                                ).add_field(
                                                                    name='📆 `| Criado em`',
                                                                    value=usuario.created_at.strftime('%d/%m/%y (%H:%M)')
                                                                ).add_field(
                                                                    name="<:DiscordDev:507925579245551616> `| Biblioteca`",
                                                                    value=lang.content
                                                                ).add_field(
                                                                    name='<:parceiro:510894109758586901> `| Criador`',
                                                                    value=f"**{message.author}**\n`{message.author.id}`"
                                                                ).add_field(
                                                                    name='<:Clyde:510894094877327360> `| Prefixo`',
                                                                    value=prefix.content
                                                                ).add_field(
                                                                    name='📋 `| Descrição`',
                                                                    value="```Nenhuma```"
                                                                ).add_field(
                                                                    name='🚀 `| Convite`',
                                                                    value=f"[link](https://discordapp.com/oauth2/authorize?client_id={usuario.id}&scope=bot&permissions=)"
                                                                )
                                                                forms.remove(message.author.id)
                                                                msg = await client.get_channel(507570211499671576).send(embed=pendenteEm)  
                                                                
                                                                await msg.add_reaction(":correto:515523764297924618")
                                                                await msg.add_reaction(":incorreto:515523818358571039")
                                                                
                                                                def opt_check(reaction, user):
                                                                    return reaction.message.id == msg.id and str(reaction.emoji) in ['<:correto:515523764297924618>', '<:incorreto:515523818358571039>'] 
                                                                            
                                                                try:
                                                                    
                                                                    reaction, user = await client.wait_for("reaction_add", check=opt_check, timeout=172800)
                                                                    
                                                                except asyncio.TimeoutError:
                                                                    await author.send(f"Olá **{author.name}**, o seu bot `{usuario}` foi automaticamente rejeitado devido se passarem **2 dias** sem resposta, reenvie novamente.")
                                                                    await msg.clear_reactions()    
                                                                
                                                                else:      
                                                                    if str(reaction.emoji) == '<:correto:515523764297924618>':
                                                                        await msg.delete()
                                                                        await logs.send(f"<:correto:510894022861127680> | {message.author.mention}, seu bot `{usuario}` foi **aceito** pelo **{user.name}**.")
                                                                        await author.send(f"<:correto:510894022861127680> | O seu bot `{usuario}` foi **aceito** pelo **{user.name}**;")

                                                                    elif str(reaction.emoji) == '<:incorreto:515523818358571039>':
                                                                        mtv1 = await client.get_channel(507570211499671576).send(f"**{user.name}**, diga o **motivo** para **recusar** o bot `{usuario}`: `(2 minutos)`")
                                                                                
                                                                        def check(m):
                                                                            return m.author == user and m.channel.id == mtv1.channel.id
                                                                                    
                                                                        try:
                                                                            mtv = await client.wait_for('message', check=check, timeout=120)
                                                                                
                                                                        except asyncio.TimeoutError:
                                                                            await mtv1.delete()
                                                                            await msg.delete()
                                                                            await logs.send(f"<:incorreto:510894050103263245> | {message.author.mention}, seu bot `{usuario}` foi **recusado** pelo **{user.name}**.\nMotivo:```Nenhum motivo informado```")
                                                                            await author.send(f"<:incorreto:510894050103263245> | O seu bot `{usuario}` foi **recusado** pelo **{user.name}**.\nMotivo:```Nenhum motivo informado```")

                                                                        else:

                                                                            if mtv.content == mtv.content:
                                                                                await mtv1.delete()
                                                                                await msg.delete()
                                                                                await logs.send(f"<:incorreto:510894050103263245> | {message.author.mention}, seu bot `{usuario}` foi **recusado** pelo **{user.name}**.\nMotivo:```{mtv.content}```")
                                                                                await author.send(f"<:incorreto:510894050103263245> | O seu bot `{usuario}` foi **recusado** pelo **{user.name}**.\nMotivo:```{mtv.content}```")
                                                                                return
                                        
                    
                except Exception as e:
                    forms.remove(message.author.id)
                    print(e)    
            
        except discord.Forbidden:
            await author.send(f"**{message.author.name}, para iniciar o processo precisamos que você libere suas mensagens privadas.**")


client.run(os.environ.get("token"))
