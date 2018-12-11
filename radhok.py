# Import

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import youtube_dl
import random
from os import environ
import asyncio
import time
import random
import datetime
import math
import requests
import random
import datetime
import math
import requests
import sys
import base64
import hashlib
import traceback
import string
import inspect
import json
import aiohttp
import websockets
import urllib.request
import logging
from collections import Counter
import os
import colorsys
import socket
import discord
from discord.ext import commands
from discord.ext.commands import Bot
from os import environ
from lxml import html
import asyncio
import time
import random
import datetime
import math
import requests
import sys
import base64
import hashlib
import traceback
import string
import inspect
import json
from cleverwrap import CleverWrap
import config
import utils
import aiohttp
import websockets
from bs4 import BeautifulSoup
import urllib.request
import logging
import colorsys
import socket




# Prefix


bot = Bot(description="Coco BOT is best", command_prefix=">", pm_help =True)

players = ()

print(f"Connecting your bot to discord!")


# Token

Token = 'my_token'


# Variables


copyright = "Copyright © 2018 Coco"


OWNER_ID = "351390806101327883"


noperm = "Sorry but you do not have permission to use that command!"


botid = "24791747004989441"



lines = "3.5k+"


if_statements = "Undefined"


else_statements = "Undefined"


total_commands = str(len(bot.commands))


total_embeds = "154"


total_variables = "Undefined"


total_imports = "Undefined"


total_dogs = "872"

DMs = "I sent 📝 you the information, Check your DMs 💌"



total_links = "Undefined"



total_dad_jokes = "382"


changelogs = "To view the change log please use the command `>changelog`"


no_work = f"This command is currently not working, Please DM Coco#6429 about the command so he can fix this issue"


user = 'Coco#6429'


key = 'q8Di3LCIL0Qny7IiwN3jxfyBuY37c9nk'



secondnoperm = "You probally have no permission to use this command or i don't have permission to do what you want me to do"


botavatar = "https://cdn.discordapp.com/avatars/507241518524923904/e258eb66f623cb34a2da8eee3d02fd1d.webp?size=1024"

giphylol = environ.get("GIPHY_TOKEN")


detoken = Token


dbltoken = environ.get('DBL_TOKEN')


dbl_url = "https://discordbots.org/api/bots/24791747004989441/stats"


headers = {"Authorization" : dbltoken}



#chatbot = ChatBot 'Coco BOT',


 #   storage_adapter='chatterbot.storage.SQLStorageAdapter',


  #  trainer='chatterbot.trainers.ChatterBotCorpusTrainer',


   # #input_adapter='chatterbot.input.TerminalAdapter',


    ##output_adapter='chatterbot.output.TerminalAdapter',


    #logic_adapters=[


     #   'chatterbot.logic.MathematicalEvaluation',


    #    'chatterbot.logic.TimeLogicAdapter',


     #   "chatterbot.logic.BestMatch"


    #],


    #database='./database.sqlite3',


#)





# Remove help


bot.remove_command('help')



async def status_task():
    while True:
        await bot.change_presence(game=discord.Game(name='>help | Coco#6429', type=2))
        await asyncio.sleep(10)
        await bot.change_presence(game=discord.Game(name='with '+str(len(set(bot.get_all_members())))+' users | >help | Coco#6429'))
        await asyncio.sleep(10)
        await bot.change_presence(game=discord.Game(name='in '+str(len(bot.servers))+' servers | >help | Coco#6429', type=3))
        await asyncio.sleep(10)



def FindDuplicates(n_list):


    unique = set(in_list)


    for each in unique:


        count = in_list.count(each)


        if count > 2:


            print('There are duplicates in this list')


    return True


    print('There are no duplicates in this list')


    return False





def get_uptime(*, brief=False):


    now = datetime.datetime.utcnow()


    delta = now - bot.uptime


    hours, reainder = divmod(int(delta.total_seconds()), 3600)


    minutes, seconds = divmod(remainder, 60)


    days, hours = divmod(hours, 24)





    if not brief:


        if days:


            fmt = '{d} days, {h} hours, {m} minutes, and {s} seconds'


        else:


            fmt = '{h} hours, {m} inutes, and {s} seconds'


    else:


        fmt = '{h}h {m}m {s}s'


        if days:


            fmt = '{d}d ' + fmt





    return fmt.format(d=days, h=hours, m=minutes, s=seconds)





# On ready


@bot.event


async def on_ready():





    print(f'Ready')
    print(f"[][][][][][][][][][][][][][][][][][][][][][][][][][]")
    print(f'Coco BOT IS ONLINE')
    print(f'Lets play')



    payload = {"server_count"  : len(bot.servers)}


    bot.loop.create_task(status_task())


    for x in range(99999999999999999999999999999999999999999999999):


        await asyncio.sleep(10)


@bot.command(pass_context = True)
async def ping(ctx):
    channel = ctx.message.channel
    t1 = time.perf_counter()
    await bot.send_typing(channel)
    t2 = time.perf_counter()
    await bot.say("Ping: {}ms".format(round((t2-t1)*1000)))



# Check


@bot.command(pass_context=True)


async def check(ctx):


    embed = dicord.Embed(title="Coco BOT is online!", color=0x29ba9e)


    await bot.say(embed=embed)


    try:


        await bot.add_reaction(ctx.message, "👍")


    except:


        pass





@bot.command(aliases=['chatbot'], pass_context=True)


async def chaton(ctx):


    await bot.say("Command disabled because it is currently being improved")





# Userinfo


@bot.command(pass_context=True)


async def userinfo(ctx, user: discord.Member):


    embed = discord.Embed(title="{}'s information".format(user.name), color=0xacd5b6)


    embed.add_field(name="Name", value=user.mention, inline=True)


    embed.add_field(name="ID", value=user.id, inline=True)


    embed.add_field(name="Status", value=user.status, inline=True)


    embed.add_field(name="Highest Role", value=user.top_role)


    embed.add_field(name="Joined", value=user.joined_at.strftime("%d %b %Y %H:%M"))


    embed.add_field(name="Created", value=user.created_at.strftime("%d %b %Y %H:%M"))


    embed.add_field(name="Color", value=user.color)


    embed.add_field(name="Bot", value=str(user.bot))


    embed.add_field(name="Playing", value=user.game)


    embed.add_field(name="Discord Tag", value=user.discriminator)


    embed.add_field(name="Nickname", value=user.nick)


    embed.add_field(name="Server", value=user.server)





    try:


            roles = [x.name for x in user.roles if x.name != "@everyone"]





            if roles:


                roles = sorted(roles, key=[x.name for x in ctx.message.server.role_hierarchy


                                           if x.name != "@everyone"].index)


                roles = ", ".join(roles)


            else:


                roles = "None"


            embed.add_field(name="Roles", value=roles)


    except:


        pass





    embed.set_thumbnail(url=user.avatar_url)


    await bot.say(embed=embed)





# Botinfo


@bot.command(pass_context=True)


async def botinfo(ctx):


    # Vars


    cpu = ["96%", "94%", "98%", "92%", "93%", "89%", "95%", "99%", "91%", "97%"]





    embed = discord.Embed(title="Coco BOTs information", color=0xD2DCE5)


    embed.add_field(name="Bot Name", value="Coco")


    embed.add_field(name="Bot Tag", value="9026")


    embed.add_field(name="Bot ID", value=botid)


    embed.add_field(name="Bot owners", value="Coco#6429")


    embed.add_field(name="Bot Prefix", value=">")


    embed.add_field(name="Bot LIB", value="discord.py")


    embed.add_field(name="Bot Language", value="Python")


#    embed.add_field(name="Bot Support Server", value="[Server Link]( )")


    embed.add_field(name="Bot Servers", value=len(bot.servers))


    embed.add_field(name="Bot Users", value=(len(set(bot.get_all_members()))))


    embed.add_field(name="Bot Commands", value=(str(len(bot.commands))))


    embed.add_field(name="Bot Invite", value="[👉 Invite my bot HERE 👈]( https://discordapp.com/api/oauth2/authorize?client_id=507241518524923904&,permissions=8&scope=bot)")

    embed.add_field(name="Donation Link", value="[Support our bot by Donating us HERE](https://paypal.me/CocoGT)")


#    embed.add_field(name="Bot Hosting Servers", value="Heroku : Online\nPC : Online\nGithub : Online")


#    embed.add_field(name="Bot Database", value="Lost")


#    embed.add_field(name="Bot Database Backup", value="PC")


#    embed.add_field(name="Bot CPU Percentage", value=random.choice(cpu))


#    embed.add_field(name="Bot Regular Boot Time", value="2.5s")


#    embed.add_field(name="Bot Virtual Memory", value="2 GB")


#    embed.add_field(name="Bot CPU Speed", value="3.8 GHz")


#    embed.add_field(name="Bot Website", value="[Click Here](https://Coco BOT-discord.github.io/index.html)")


    embed.set_thumbnail(url=" ")


    await bot.say(embed=embed)

# math

@bot.command()
async def add(left : int, right : int):
    """Adds two numbers together."""
    await bot.say(left + right)

@bot.command()
async def substract(left : int, right : int):
    """Subtracts two numbers together."""
    await bot.say(left - right)

@bot.command()
async def divide(left : int, right : int):
    """Divides two numbers together."""
    await bot.say(left / right)

@bot.command()
async def multiply(left : int, right : int):
    """Multiplies two numbers together."""
    await bot.say(left * right)

# Serverinfo


@bot.command(pass_context=True)


async def serverinfo(ctx):

    server = ctx.message.server


    online = len([m.status for m in ctx.message.server.members


                    if m.status == discord.Status.online or


                    m.status == discord.Status.idle])





    embed = discord.Embed(name="{} Server information".format(ctx.message.server.name), color=0xffe5f3)


    embed.add_field(name="Server name", value=ctx.message.server.name, inline=True)


    embed.add_field(name="Owner", value=ctx.message.server.owner.mention)


    embed.add_field(name="Server ID", value=ctx.message.server.id, inline=True)


    embed.add_field(name="Roles", value=len(ctx.message.server.roles), inline=True)


    embed.add_field(name="Members", value=len(ctx.message.server.members), inline=True)


    embed.add_field(name="Online", value=f"**{online}/{len(ctx.message.server.members)}**")


    embed.add_field(name="Created at", value=ctx.message.server.created_at.strftime("%d %b %Y %H:%M"))


    embed.add_field(name="Emojis", value=f"{len(ctx.message.server.emojis)}/100")


    embed.add_field(name="Server Region", value=str(ctx.message.server.region).title())


    embed.add_field(name="Total Channels", value=len(ctx.message.server.channels))


    embed.add_field(name="AFK Channel", value=str(ctx.message.server.afk_channel))


    embed.add_field(name="AFK Timeout", value=ctx.message.server.afk_timeout)


    embed.add_field(name="Verification Level", value=ctx.message.server.verification_level)


    try:


        embed.add_field(name="Role Names", value=", ".join([role.name for role in ctx.message.server.roles if role.name != "@everyone"]))


    except:


        pass


    embed.set_thumbnail(url=ctx.message.server.icon_url)


    await bot.say(embed=embed)





# Shutdown


@bot.command(pass_context=True)


async def shutdown(ctx):


    if ctx.message.author.id == OWNER_ID:


        embed = discord.Embed(title="Coco BOT shutting down!", color=0xffc107)


        msg = await bot.say(embed=embed)


        await asyncio.sleep(2)


        em = discord.Embed(title="See you next time!", color=0xffc107)


        await bot.edit_message(msg, embed=em)


        await bot.delete_message(msg)


        quit()


    else:


        emd = discord.Embed(title=noperm, color=0xff0000)


        await bot.say(embed=emd)





# Restart


@bot.command(pass_context=True)


async def restart(ctx):


    if ctx.message.author.id == OWNER_ID:


        embed = discord.Embed(title="Coco BOT restarting!", color=0x008484)


        msg = await bot.say(embed=embed)


        await asyncio.sleep(2)


        em = discord.Embed(title="Coco BOT we will back!", color=0x008484)


        await bot.edit_message(msg, embed=em)


        quit()


    else:


        emd = discord.Embed(title=noperm, color=0xff0000)


        await bot.say(embed=emd)





# Servers


@bot.command(pass_context=True)


async def servers(ctx):


    if ctx.message.author.id == OWNER_ID:


        #nl = "\n"


        #stringy = ""


        #for server in bot.servers:


        #    stringy += f"{server.name} : `{server.id}`{nl}"


        #await bot.send_message(ctx.message.author, stringy)


        for server in bot.servers:


            await bot.send_message(ctx.message.author, f"{server.name}  :  `{server.id}`")


    else:


        emd = discord.Embed(title=noperm, color=0xff0000)


        await bot.say(embed=emd)





# Kick


@bot.command(pass_context=True)


async def kick(ctx, user: discord.Member):


    if ctx.message.author.server_permissions.kick_members:


        embed = discord.Embed(title="Successfully kicked {} from ".format(user.name) + (ctx.message.server.name), color=0x96bef0)


        await bot.kick(user)


        await bot.say(embed=embed)


    else:


        emd = discord.Embed(title=noperm, color=0xff0000)


        await bot.say(embed=emd)





# Ban


@bot.command(pass_context=True)


async def ban(ctx, user: discord.Member):


    if ctx.message.author.server_permissions.ban_members:


        embed = discord.Embed(title="Successfully banned {} from ".format(user.name) + (ctx.message.server.name), color=0xff6666)


        await bot.ban(user)


        await bot.say(embed=embed)


    else:


        emd = discord.Embed(title=noperm, color=0xff0000)


        await bot.say(embed=emd)



# Invite

@bot.command(pass_context=True)


async def invite(ctx):


    embed = discord.Embed(title="Please support Coco BOT by inviting it on your server and donate if you want to improve the bot", color=0xD2DCE5)


    embed.add_field(name="Here is my bot invite link", value="[Click here to invite Coco BOT] (https://discordapp.com/api/oauth2/authorize?client_id=507241518524923904&permissions=8&scope=bot)")

    embed.add_field(name="Donation Link", value="[Support our bot by donating us :)] (https://paypal.me/CocoGT)")


    await bot.say(embed=embed)





# Membercount


@bot.command(pass_context=True)


async def membercount(ctx):


    embed = discord.Embed(title="The total amount of members in {}".format(ctx.message.server.name), description=len(ctx.message.server.members), color=0x17a2b8)


    embed.set_thumbnail(url=ctx.message.server.icon_url)


    await bot.say(embed=embed)





# Servercount


@bot.command(pass_context=True)


async def servercount(ctx):


    embed = discord.Embed(title="Server Counter", description=len(bot.servers), color=0xff6800)


    await bot.say(embed=embed)





# Websiteip


@bot.command(pass_context=True)


async def websiteip(ctx):


    embed = discord.Embed(title="IP Addresses of famous websites", color=0x7564cb)





    google = socket.gethostbyname('google.com')


    stack = socket.gethostbyname('stockoverflow.com')


    discordapp = socket.gethostbyname('discordapp.com')


    youtube = socket.gethostbyname('youtube.com')


    github = socket.gethostbyname('github.com')


    instagram = socket.gethostbyname('instagram.com')


    twitter = socket.gethostbyname('twitter.com')


    twitch = socket.gethostbyname('twitch.tv')


    amazon = socket.gethostbyname('amazon.com')


    facebook = socket.gethostbyname('facebook.com')


    imgur = socket.gethostbyname('imgur.com')


    wiki = socket.gethostbyname('wikipedia.org')


    ted = socket.gethostbyname('ted.com')


    baidu = socket.gethostbyname('baidu.com')


    netflix = socket.gethostbyname('netflix.com')


    bing = socket.gethostbyname('bing.com')


    pornhub = socket.gethostbyname('pornhub.com')








    embed.add_field(name="...", value=f"Google : {google}\n"


                                      f"Stackoverflow : {stack}\n"


                                      f"Discord : {discordapp}\n"


                                      f"YouTube : {youtube}\n"


                                      f"GitHub : {github}\n"


                                      f"Instagram : {instagram}\n"


                                      f"Twitter : {twitter}\n"


                                      f"Twitch : {twitch}\n"


                                      f"Amazon : {amazon}\n"


                                      f"Facebook : {facebook}\n"


                                      f"Imgur : {imgur}\n"


                                      f"Wiki : {wiki}\n"


                                      f"Ted : {ted}\n"


                                      f"Baidu : {baidu}\n"


                                      f"Netflix : {netflix}\n"


                                      f"Bing : {bing}\n"


                                      f"PornHub : {pornhub}")


    await bot.say(embed=embed)





# Avatar


@bot.command(pass_context=True)


async def avatar(ctx, user: discord.Member):


    embed = discord.Embed(title="{}'s Avatar".format(user.name), color=0xfff799)


    embed.set_image(url=user.avatar_url)


    await bot.say(embed=embed)





# Playing


@bot.command(pass_context=True)


async def playing(ctx, type: int, *, changeto : str):


    if ctx.message.author.id == OWNER_ID:


        game = (discord.Game(name=changeto, url="https://twitch.tv/myname", type=type))


        await bot.change_presence(game=game)


        await bot.say("Sucessfully changed!")


    else:


        emd = discord.Embed(title=noperm, color=0xff0000)


        await bot.say(embed=emd)





# Slow Purge


@bot.command(pass_context=True)


async def slowpurge(ctx):


    try:


        if ctx.message.author.server_permissions.manage_messages:


            async for msg in bot.logs_from(ctx.message.channel):


                await bot.delete_message(msg)


        else:


            emd = discord.Embed(title=noperm, color=0xff0000)


            await bot.say(embed=emd)


    except Exception as e:


        await bot.say(e)





# Warn


@bot.command(pass_context=True)


async def warn(ctx, member : discord.Member = None, *, message):


    if ctx.message.author.server_permissions.ban_members:


        if member == "@everyone":


            await bot.send_message(member, message)


        else:


            await bot.send_message(member, "Warning From {} Admins : ".format(ctx.message.server.name) + message)


        await bot.send_message(ctx.message.author, "Successfully warned *{}*".format(member.mention))


    else:


        emd = discord.Embed(title=noperm, color=0xff0000)


        await bot.say(embed=emd)





# Dm


@bot.command(pass_context=True)


async def dm(ctx, member : discord.Member = None, *, message):


    if ctx.message.author.id == OWNER_ID:


        if member == "@everyone":


            await bot.send_message(member, message)


        else:


            await bot.send_message(member, message)


        await bot.send_message(ctx.message.author, "Successfully dmed *{}*".format(member.mention))


    else:


        emd = discord.Embed(title=noperm, color=0xff0000)


        await bot.say(embed=emd)





# Decide


@bot.command(pass_context=True)


async def decide(ctx):


    if ctx.message.author.server_permissions.kick_members:


        decided = ["Ban him", "Kick him", "Do whatever you wanna do!"]


        embed = discord.Embed(title=random.choice(decided), color=0xff9c9c)


        await bot.say(embed=embed)


    else:


        emd = discord.Embed(title=noperm, color=0xff0000)


        await bot.say(embed=emd)





# Secret ban


@bot.command(pass_context=True)


async def secretban(ctx, user: discord.Member = None):


    if ctx.message.author.server_permissions.ban_members:


        if user == None:


            await bot.send_message(ctx.message.author, "```Proper usage is\n\n>secretban <mention a user to secretly ban```>")


        else:


            await bot.ban(user)


    else:


        emd = discord.Embed(title=noperm, color=0xff0000)


        await bot.say(embed=emd)





# Secret kick


@bot.command(pass_context=True)


async def secretkick(ctx, user: discord.Member = None):


    try:


        if ctx.message.author.server_permissions.kick_members:


            if user == None:


                await bot.send_message(ctx.message.author, "Proper usage is\n\n>secretkick <mention a user to secretly kick>")


            else:


                await bot.kick(user)


        else:


            emd = discord.Embed(title=noperm, color=0xff0000)


            await bot.say(embed=emd)


    except Exception as e:


        await bot.send_message(ctx.message.author, e)





# Say


@bot.command(pass_context=True)


async def say(ctx, *, what_to_say : str):


    if ctx.message.author.id == OWNER_ID:


        await bot.say(what_to_say)


    else:


        await bot.say(f"{ctx.message.author.mention} Said : " + what_to_say)





# Embed


@bot.command(pass_context=True)


async def embed(ctx, *, what_to_say : str):


    colors = [0x7a58d4, 0xff0027, 0x00fff2, 0x00ff09, 0xb5fff8, 0xb5b8ff, 0xffc300, 0xff99b8]


    randomizer = random.choice(colors)


    if ctx.message.author.id == OWNER_ID:


        await bot.delete_message(ctx.message)


        embed = discord.Embed(title=what_to_say, color=randomizer)


        await bot.say(embed=embed)


    else:


        embed2 = discord.Embed(title=f"{ctx.message.author.name} Said : ", description=what_to_say, color=0x7a58d4)


        await bot.delete_message(ctx.message)


        await bot.say(embed=embed2)





# QR Code


@bot.command(pass_context=True)


async def qr(ctx, *, message: str):


    new_message = message.replace(" ", "+")


    url = f"http://api.qrserver.com/v1/create-qr-code/?data={new_message}"





    embed = discord.Embed(color=0xe73131)


    embed.set_image(url=url)


    await bot.say(embed=embed)





# Google


@bot.command(pass_context=True)


async def google(ctx, *, message):


    new_message = message.replace(" ", "+")


    url = f"https://www.google.com/search?q={new_message}"


    await bot.say(url)





# Youtube


@bot.command(pass_context=True)


async def youtube(ctx, *, message: str):


    new_message = message.replace(" ", "+")


    url = f"https://www.youtube.com/results?search_query={new_message}"





    await bot.say(url)





# Meme


@bot.command(pass_context=True)


async def meme(ctx):


    embed = discord.Embed(color=0xf45f5f)


    embed.set_image(url=random.choice(config.memes))


    await bot.say(embed=embed)





# Ask


@bot.command(pass_context=True)


async def ask(ctx, *, question: str):


    answer = ["No", "Yes", "Obviously a yes", "Obviously a no", "OBAMA!", "Heck Yeah!", "Please no", "Im gonna die", "hell yeah!", "Fuck no!", "Hell Naw!", "Hell Yeah!", "Yes please", "Just don't", "FBI!"]


    randomizer = random.choice(answer)


    embed = discord.Embed(title=question, description=f"{randomizer}", color=0xefff00)


    await bot.say(embed=embed)





# Kiss


@bot.command(pass_context=True)


async def kiss(ctx, user: discord.Member):


    randomurl = ["https://media3.giphy.com/media/G3va31oEEnIkM/giphy.gif", "https://i.imgur.com/eisk88U.gif", "https://media1.tenor.com/images/e4fcb11bc3f6585ecc70276cc325aa1c/tenor.gif?itemid=7386341", "http://25.media.tumblr.com/6a0377e5cab1c8695f8f115b756187a8/tumblr_msbc5kC6uD1s9g6xgo1_500.gif"]


    if user.id == ctx.message.author.id:


        await bot.say("Goodluck kissing yourself {}".format(ctx.message.author.mention))


    else:


        if user.id == botid:


            await bot.say("Ewww don't try to kiss me")


        else:


            embed = discord.Embed(title=f"{user.name} You just got a kiss from {ctx.message.author.name}", color=0xd0a3d0)


            embed.set_image(url=random.choice(randomurl))


            await bot.say(embed=embed)





# Hug


@bot.command(pass_context=True)


async def hug(ctx, user: discord.Member):


    if user.id == ctx.message.author.id:


        await bot.say("{} Wanted to hug his self, good luck on that you will look like an idiot trying to do it".format(user.mention))


    else:


        if user.id == botid:


            await bot.say("You will turn into a metal if you hug me")


        else:


            randomurl = ["http://gifimage.net/wp-content/uploads/2017/09/anime-hug-gif-5.gif", "https://media1.tenor.com/images/595f89fa0ea06a5e3d7ddd00e920a5bb/tenor.gif?itemid=7919037", "https://media.giphy.com/media/NvkwNVuHdLRSw/giphy.gif"]


            embed = discord.Embed(title=f"{user.name} You just got a hug from {ctx.message.author.name}", color=0xafeeee)


            embed.set_image(url=random.choice(randomurl))


            await bot.say(embed=embed)





# Gender


@bot.command(pass_context=True)


async def gender(ctx, user: discord.Member):


    random.seed(user.id)


    genderized = ["Male", "Female", "Transgender", "Unknown", "Can't be detected", "Error 404 gender type cannot be found in the database"]


    randomizer = random.choice(genderized)


    if user == ctx.message.author:


        embed = discord.Embed(title="You should know your own gender", color=0xfff47d)


        await bot.say(embed=embed)


    else:


        embed = discord.Embed(color=0xfff47d)


        embed.add_field(name=f"{user.name}'s gender check results", value=f"{randomizer}")


        await bot.say(embed=embed)





# Virgin


@bot.command(pass_context=True)


async def virgin(ctx, user: discord.Member):


    random.seed(user.id)


    results= ["No longer a virgin", "Never been a virgin", "100% Virgin", "Half virgin :thinking:", "We cannot seem to find out if this guy is still a virgin due to it's different blood type"]


    randomizer = random.choice(results)


    if user == ctx.message.author:


        embed = discord.Embed(title="Go ask yourself if you are still a virgin", color=0x7dfff2)


        await bot.say(embed=embed)


    else:


        embed = discord.Embed(color=0x7dfff2)


        embed.add_field(name=f"{user.name}'s virginity check results", value=f"{randomizer}")


        await bot.say(embed=embed)





# FBI


@bot.command(pass_context=True)


async def fbi(ctx):


    msg = await bot.say("Contacting the FBI")


    await asyncio.sleep(3)


    await bot.edit_message(msg, "Successfully contacted the FBI")


    await asyncio.sleep(1)


    msg2 = await bot.say(f"Looking for {ctx.message.author.mention}'s home address")


    await asyncio.sleep(2)


    await bot.edit_message(msg2, "Successfully found the home address")


    msg3 = await bot.say(f"Sending the FBI to {ctx.message.author.mention}'s house")


    await asyncio.sleep(1)


    msg4 = await bot.say(f"According to my calculations it will take about 20 seconds before the FBI gets to {ctx.message.author.mention}'s house")


    await asyncio.sleep(20)


    await bot.edit_message(msg3, "FBI Sent!")


    await bot.edit_message(msg4, "Ok it is now done!")


    await bot.send_message(ctx.message.author, "FBI!")


    await asyncio.sleep(1)


    await bot.send_message(ctx.message.author, "FBI!")


    await asyncio.sleep(1)


    await bot.send_message(ctx.message.author, "FBI!")


    await asyncio.sleep(1)


    await bot.send_message(ctx.message.author, "FBI!")


    await asyncio.sleep(1)


    await bot.send_message(ctx.message.author, "FBI!")


    await asyncio.sleep(1)


    await bot.send_message(ctx.message.author, "The FBI is here")


    await asyncio.sleep(1)


    await bot.send_message(ctx.message.author, "Please put your hands up in the air while we investigate your internet browser")


    await asyncio.sleep(1)


    await bot.send_message(ctx.message.author, "Don't fucking MOVE!")


    await asyncio.sleep(1)


    await bot.send_message(ctx.message.author, "If you move you are going to die!")


    await asyncio.sleep(1)


    await bot.send_message(ctx.message.author, "Ok we have successfully investigated your internet browser and we found out you have some porn in your history\nplease consider coming with us")





# Joke


@bot.command(pass_context=True)


async def joke(ctx):


    joke = ["What do you call a frozen dog?\nA pupsicle", "What do you call a dog magician?\nA labracadabrador", "What do you call a large dog that meditates?\nAware wolf", "How did the little scottish dog feel when he saw a monster\nTerrier-fied!", "Why did the computer show up at work late?\nBecause it had a hard drive", "Autocorrect has become my worst enime", "What do you call an IPhone that isn't kidding around\nDead Siri-ous", "The guy who invented auto-correct for smartphones passed away today\nRestaurant in peace", "You know you're texting too much when you say LOL in real life, instead of laughing", "I have a question = I have 18 Questions\nI'll look into it = I've already forgotten about it", "Knock Knock!\nWho's there?\Owls say\nOwls say who?\nYes they do.", "Knock Knock!\nWho's there?\nWill\nWill who?\nWill you just open the door already?", "Knock Knock!\nWho's there?\nAlpaca\nAlpaca who?\nAlpaca the suitcase, you load up the car.", "Yo momma's teeth is so yellow, when she smiled at traffic, it slowed down.", "Yo momma's so fat, she brought a spoon to the super bowl.", "Yo momma's so fat, when she went to the beach, all the whales started singing 'We are family'", "Yo momma's so stupid, she put lipstick on her forehead to make up her mind.", "Yo momma's so fat, even Dora can't explore her.", "Yo momma's so old, her breast milk is actually powder", "Yo momma's so fat, she has to wear six different watches: one for each time zone", "Yo momma's so dumb, she went to the dentist to get a bluetooth", "Yo momma's so fat, the aliens call her 'the mothership'", "Yo momma's so ugly, she made an onion cry.", "Yo momma's so fat, the only letters she knows in the alphabet are K.F.C", "Yo momma's so ugly, she threw a boomerang and it refused to come back", "Yo momma's so fat, Donald trump used her as a wall", "Sends a cringey joke\nTypes LOL\nFace in real life : Serious AF", "I just got fired from my job at the keyboard factory. They told me I wasn't putting enough shifts.", "Thanks to autocorrect, 1 in 5 children will be getting a visit from Satan this Christmas.", "Have you ever heard about the new restaurant called karma?\nThere's no menu, You get what you deserve.", "Did you hear about the claustrophobic astronaut?\nHe just needed a little space", "Why don't scientists trust atoms?\nBecase they make up everything", "How did you drown a hipster?\nThrow him in the mainstream", "How does moses make tea?\nHe brews", "A man tells his doctor\n'DOC, HELP ME. I'm addicted to twitter!'\nThe doctor replies\n'Sorry i don't follow you...'", "I told my wife she was drawing her eyebrows too high. She looked surprised.", "I threw a boomeranga a few years ago. I now live in constant fear"]


    embed = discord.Embed(color=0x5e72a2)


    embed.add_field(name=f"Here is a random joke that {ctx.message.author.name} requested", value=random.choice(joke))


    await bot.say(embed=embed)





# Dadjoke


@bot.command(pass_context=True)


async def dadjoke(ctx):


    dadjoke = ["Why did the girl show her boobs to the paper factory?\nTo make flash paper", "My dad literally told me this one last week: 'Did you hear about the guy who invented Lifesavers? They say he made a mint.", "A ham sandwich walks into a bar and orders a beer. Bartender says, 'Sorry we don't serve food here.", "Me: 'Dad, make me a sandwich!' Dad: 'Poof, You’re a sandwich!'", "Why did the Clydesdale give the pony a glass of water?  Because he was a little horse!", "How do you make a Kleenex dance? Put a little boogie in it!", "Two peanuts were walking down the street. One was a salted.", "What time did the man go to the dentist? Tooth hurt-y.", "I'm reading a book about anti-gravity. It's impossible to put down!", "You're American when you go into the bathroom, and you're American when you come out, but do you know what you are while you're in there? European.", "Did you know the first French fries weren't actually cooked in France? They were cooked in Greece.", "Want to hear a joke about a piece of paper? Never mind... it's tearable.", "I just watched a documentary about beavers. It was the best dam show I ever saw!", "If you see a robbery at an Apple Store does that make you an iWitness?", "Spring is here! I got so excited I wet my plants!", "A ham sandwich walks into a bar and orders a beer. The bartender says, 'Sorry we dont serverserver food here.", "What’s Forrest Gump’s password? 1forrest1", "Why did the Clydesdale give the pony a glass of water?  Because he was a little horse!", "Did you hear about the guy who invented Lifesavers? They say he made a mint.", "I bought some shoes from a drug dealer. I don't know what he laced them with, but I was tripping all day!", "Why do chicken coops only have two doors? Because if they had four, they would be chicken sedans!", "What do you call a factory that sells passable products? A satisfactory.", "How do you make a Kleenex dance? Put a little boogie in it!", "When a dad drives past a graveyard: Did you know that's a popular cemetery? Yep, people are just dying to get in there!", "Two peanuts were walking down the street. One was a salted.", "Why did the invisible man turn down the job offer? He couldn't see himself doing it.", "I used to have a job at a calendar factory but I got the sack because I took a couple of days off.", "How do you make holy water? You boil the hell out of it.", "When you ask a dad if he's alright: 'No, I’m half left.'", "I had a dream that I was a muffler last night. I woke up exhausted!", "Did you hear the news? FedEx and UPS are merging. They’re going to go by the name Fed-Up from now on.", "5/4 of people admit that they’re bad with fractions.", "MOM : How do i look?\nDad : With your eyes.", "What is Beethoven’s favorite fruit? A ba-na-na-na.", "Two guys walk into a bar, the third one ducks.", "What do you call a masturbating cow? Beef Stroganoff.", "Did you hear about the circus fire? It was in tents!", "Don't trust atoms. They make up everything!", "What do you call a cow with two legs? Lean beef. If the cow has no legs, then it’s ground beef.", "What do you get when you cross an elephant with a rhino? Elephino.", "How many tickles does it take to make an octopus laugh? Ten-tickles.", "I’m only familiar with 25 letters in the English language. I don’t know why.", "What's the best part about living in Switzerland? I don't know, but the flag is a big plus."]


    embed = discord.Embed(color=0x20bb2a)


    embed.add_field(name=f"Here is a random joke that {ctx.message.author.name} requested", value=random.choice(dadjoke))


    await bot.say(embed=embed)


    async with aiohttp.botSession(headers={"Accept": "application/json"}) as cs:


        async with cs.get('https://icanhazdadjoke.com/') as r:


            res = await r.json()


            embed = discord.Embed(description=res['joke'], color=0xf45f5f)


            await bot.say(embed=embed)





# Skincolor


@bot.command(pass_context=True)


async def skincolor(ctx, user: discord.Member):


    random.seed(user.id)


    skins = ["White", "Black", "Blue", "Green", "Rainbow", "Purple", "Brown", "Pink", "Cream", "Orange"]


    if user == ctx.message.author:


        embed2 = discord.Embed(title="You should know your own skin color", color=0xcb287a)


        await bot.say(embed=embed2)


    else:


        embed = discord.Embed(color=0xcb287a)


        embed.add_field(name=f"{user.name}'s skin color", value=random.choice(skins))


        await bot.say(embed=embed)





# Imports


@bot.command(pass_context=True)


async def imports(ctx):


    embed = discord.Embed(color=0x17e170)


    embed.add_field(name="Coco BOT's imports", value="```py\nfrom bs4 import BeautifulSoup\nimport websockets\nimport aiohttp\nimport utils\nimport config\nimport json\nfrom cleverwrap import CleverWrap\nimport inspect\nimport discord\nfrom discord.ext import commands\nfrom discord.ext.commands import Bot\nfrom os import environ\nimport asyncio\nimport time\nimport random\nimport datetime\nimport math\nimport requests\nimport sys\nimport base64\nimport hashlib\nimport traceback\nimport string\nfrom lxml import html```")


    await bot.say (embed=embed)





# Encode


@bot.command(pass_context=True)


async def encode(ctx, *, encode_to: str):


    try:


        encoded = hashlib.md5(encode_to.encode('utf-8')).hexdigest()


        await bot.say(embed=discord.Embed(color=0x003cff, title=f"{encode_to} has been encoded to md5 results are below",


                                        description=f"{encoded}"))


    except Exception as e:


        await bot.say(f"Could not encode.\n`{e}`")





# Vars


@bot.command(pass_context=True)


async def vars(ctx):


    embed = discord.Embed(color=0x5f00a4)


    embed.add_field(name="Coco BOT's basic variables", value='```py\ncopyright = "Copyright © 2018 Coco"\nOWNER_ID = "351390806101327883"\nnoperm = "Sorry but you do not have permission to use that command!"\nbotid = "24791747004989441"\nToken = environ.get("Token")\npsc = pass_context=True\nem = embed.Discord\nuser = ctx, user: discord.Member\nstr = ctx, message: str\nstrchop = ctx, *, message: str\nblack_listed_id = "None"\nstrmember = ctx, *, user: discord.Member, message: str\nstrint = ctx, *, message: str, no: int```')


    await bot.say(embed=embed)

# Clear


@bot.command(pass_context=True)


async def clear(ctx, amount = 1000):


    if ctx.message.author.server_permissions.manage_messages or ctx.message.author.id == OWNER_ID:


        mgs = [] #Empty list to put all the messages in the log


        number = int(number) #Converting the amount of messages to delete to an integer


        async for x in bot.logs_from(ctx.message.channel, limit=int(amount) +1):


            mgs.append(x)


        await bot.delete_messages(mgs)
        await bot.say(str(amount) + ' messages were deleted')

    else:


        emd = discord.Embed(title=noperm, color=0xff0000)


        await bot.say(embed=emd)



# Dox


@bot.command(pass_context=True)


async def dox(ctx):


    embed = discord.Embed(title="LEET DOX V1.0", description="Note : This tool is just for fun and it is completely fake to continue please type in >startdox and mention a user then hit enter", color=0xb39e0d)


    await bot.say(embed=embed)





# Startdox


@bot.command(pass_context=True)


async def startdox(ctx, user: discord.Member):


    random.seed(user.id)


    msg = await bot.say(f"Checking if {user.mention} is a bot user")


    await asyncio.sleep(2)


    if user.bot:


        await bot.edit_message(msg, "Sorry but you cannot dox a bot user")


        return


    else:


        await bot.edit_message(msg, f"{user.mention} is not a bot user.")


        mgs = await bot.say("Starting the dox tool")


        await asyncio.sleep(4)


        await bot.edit_message(mgs, "Dox tool successfully started")


        msg2 = await bot.say(f"Looking for {user.mention}'s information\nPlease stand by, this might take some time")


        await asyncio.sleep(20)


        embed = discord.Embed(title="LEET DOX V1.0", color=0xb39e0d)


        embed.add_field(name="Full Name", value=random.choice(config.names))


        embed.add_field(name="Gender", value=random.choice(config.gender))


        embed.add_field(name="Birthday", value=random.choice(config.birthday))


        embed.add_field(name="Security Number", value=random.choice(config.security_number))


        embed.add_field(name="Street", value=random.choice(config.street))


        embed.add_field(name="City", value=random.choice(config.city))


        embed.add_field(name="State", value=random.choice(config.state))


        embed.add_field(name="Zipcode", value=random.choice(config.zipcode))


        embed.add_field(name="Number", value=random.choice(config.number))


        embed.add_field(name="Card Type", value=random.choice(config.card_type))


        embed.add_field(name="Card Number", value=random.choice(config.card_number))


        embed.add_field(name="CVV2", value=random.choice(config.cvv2))


        embed.add_field(name="Expires", value=random.choice(config.expires))


        embed.add_field(name="Username", value=random.choice(config.username))


        embed.add_field(name="Password", value=random.choice(config.password))


        embed.add_field(name="IP Address", value=random.choice(config.ipv))


        embed.add_field(name="Race", value=random.choice(config.race))


        embed.add_field(name="Email", value=random.choice(config.email))


        embed.add_field(name="Password", value=random.choice(config.passwords))


        await bot.edit_message(msg2, embed=embed)


        await asyncio.sleep(1)


        await bot.say("Successfully found the results for {}".format(user.mention))





# IP List


@bot.command(pass_context=True)


async def iplist(ctx):


    embed = discord.Embed(color=0xd0ff2d)


    embed.add_field(name="Row 1", value="130.87.210.254\n"


                                        "75.255.127.157\n"


                                        "93.168.56.176\n"


                                        "60.3.228.219\n"


                                        "84.158.13.46\n"


                                        "6.195.148.114\n"


                                        "178.129.124.100\n"


                                        "235.179.72.23\n"


                                        "186.221.181.172\n"


                                        "46.238.208.70\n"


                                        "79.209.157.30\n"


                                        "185.141.177.240\n"


                                        "128.143.138.141\n"


                                        "104.127.11.141\n"


                                        "104.247.204.208\n"


                                        "119.55.100.155\n"


                                        "176.56.33.41\n"


                                        "239.71.204.229\n"


                                        "54.142.86.114\n"


                                        "146.104.28.93")


    embed.add_field(name="Row 2", value="21.250.255.114\n"


                                        "144.34.107.248\n"


                                        "231.213.217.70\n"


                                        "93.51.14.159\n"


                                        "56.136.44.158\n"


                                        "168.7.131.158\n"


                                        "83.156.195.95\n"


                                        "44.161.51.67\n"


                                        "251.137.174.183\n"


                                        "9.215.19.98\n"


                                        "76.211.60.146\n"


                                        "92.114.46.130\n"


                                        "181.199.172.134\n"


                                        "220.197.69.213\n"


                                        "37.19.34.0\n"


                                        "153.102.227.164\n"


                                        "80.152.173.153\n"


                                        "52.198.162.73\n"


                                        "159.158.12.218\n"


                                        "215.12.127.158")


    embed.add_field(name="Row 3", value="63.77.152.89\n"


                                        "222.206.70.122\n"


                                        "37.87.209.102\n"


                                        "197.168.84.252\n"


                                        "232.122.99.203\n"


                                        "208.181.25.221\n"


                                        "220.21.174.166\n"


                                        "129.55.229.165\n"


                                        "85.18.204.70\n"


                                        "115.237.202.150\n"


                                        "158.110.38.230\n"


                                        "243.19.227.99\n"


                                        "165.113.194.233\n"


                                        "18.32.8.1\n"


                                        "1.159.9.133\n"


                                        "15.242.37.224\n"


                                        "22.35.66.79\n"


                                        "19.49.24.80\n"


                                        "187.44.132.36\n"


                                        "111.47.88.4")


    embed.set_footer(text="This is a total of 60 IP Addresses")


    await bot.say(embed=embed)





# Namelist


@bot.command(pass_context=True)


async def namelist(ctx):


    embed = discord.Embed(color=0xdeadbf)


    embed.add_field(name="Real Names", value="Alysha Marshall\n"


                                            "Sammy Fernandez\n"


                                            "Zuzanna Mccormick\n"


                                            "Emeli Haley\n"


                                            "Marnie Savage\n"


                                            "Eleasha Fitzgerald\n"


                                            "Anthony Hope\n"


                                            "Kelsea Partridge\n"


                                            "Katelyn Shields\n"


                                            "Aine Michael\n"


                                            "Bertie North\n"


                                            "Thelma Potts\n"


                                            "Jean-Luc Chang\n"


                                            "Shanelle Holder\n"


                                            "Kirsty Wormald\n"


                                            "Conna Wilder\n"


                                            "Lexi-Mae Andrew\n"


                                            "Dilan Whitworth\n"


                                            "Bertram John\n"


                                            "Rahima Norris")


    embed.add_field(name="Rapper Names", value="Lil Bomb\n"


                                                "Lil Pump\n"


                                                "Lil Durt\n"


                                                "Lil Kid\n"


                                                "Master Rough\n"


                                                "Notorious Lil Biggie\n"


                                                "Lil Drop\n"


                                                "Lil Hack\n"


                                                "Lil Rap\n"


                                                "Lil Wayne\n"


                                                "Lil Shady\n"


                                                "Lil Spit\n"


                                                "Lil Fire\n"


                                                "Lil Hot\n"


                                                "Lil Supah\n"


                                                "Lil Epic\n"


                                                "Lil Dirty\n"


                                                "Lil Yachty\n"


                                                "Lil Dope\n"


                                                "Lil Trump")


    embed.add_field(name="Usernames", value="Latignome\n"


                                            "Falconjure\n"


                                            "Wallaby\n"


                                            "Turkiwi\n"


                                            "SmoothHazelnut\n"


                                            "CountryBeetle\n"


                                            "AncientCruncher\n"


                                            "AgilePetal\n"


                                            "SpotlessKiwi\n"


                                            "AfternoonWillow\n"


                                            "Knighthawk\n"


                                            "Raptortoise\n"


                                            "Magmaster\n"


                                            "MammothMoth\n"


                                            "GameWatermelon\n"


                                            "GlamorousMaple\n"


                                            "LightningSuccubus\n"


                                            "HarshChimpanzee\n"


                                            "PlasticHamster\n"


                                            "ArchRoach")


    await bot.say(embed=embed)





# Cardlist


@bot.command(pass_context=True)


async def cardlist(ctx):


    embed = discord.Embed(color=0x0c41ee)


    embed.add_field(name="Mastercard", value="5497210046744037\n"


                                            "5566329319369722\n"


                                            "5309140164772858\n"


                                            "5360611128738280\n"


                                            "5361183789910227\n"


                                            "5589171594935436\n"


                                            "5181117923070926\n"


                                            "5533898191447038\n"


                                            "5470860901980976\n"


                                            "5554708761694394")


    embed.add_field(name="Visa", value="4485617764743966\n"


                                        "4539307420196157\n"


                                        "4532677305001350\n"


                                        "4024007112109003\n"


                                        "4024007180797564\n"


                                        "4539047537284815\n"


                                        "4010071041781098\n"


                                        "4485754983457324\n"


                                        "4556152488628024\n"


                                        "4539144702838143")


    await bot.say(embed=embed)





# Dubstep


@bot.command(pass_context=True)


async def dubstep(ctx):


    await bot.say(f"Here is a random dubstep music that i normally listen to\n{random.choice(config.url)}")


    await bot.say(embed=embed)





# urmomgay


@bot.command(pass_context=True)


async def urmomgay(ctx):


    embed = discord.Embed(color=0x2d69ff)


    embed.add_field(name="Very noice story!", value=f"Jeff : So what do you think about my hot mom? ( ͡° ͜ʖ ͡°)\n{ctx.message.author.name} : ur mom gay\nJeff : ***dies***")


    embed.set_image(url="https://i.tweeterino.com/uploads/fake-tweet20180220-12-u5nnj5.jpg")


    msg = await bot.say(embed=embed)


    await bot.add_reaction(msg, "🇺")


    await bot.add_reaction(msg, "🇷")


    await bot.add_reaction(msg, "🇲")


    await bot.add_reaction(msg, "🇴")


    await bot.add_reaction(msg, "🇲")


    await bot.add_reaction(msg, "🇬")


    await bot.add_reaction(msg, "🇦")


    await bot.add_reaction(msg, "🇾")





# sapnupuas


@bot.command(pass_context=True)


async def sapnupuas(ctx):


    embed = discord.Embed(color=0x441ab6)


    embed.add_field(name="Meanwhile in Mccdonald's secret area", value=f"{ctx.message.author.name} : hai gerl ples kiss 1 fut penus and show vagen ples\n\nHailey : You wanna see what?\n\n{ctx.message.author.name} : ples bobs vagen insert 1 fut penus big and fell good\n\nHailey : Sorry i cannot understand you, please fix your english\n\n{ctx.message.author.name} : I came from a different planet and i am here to tell you that we are all going to die and there is only one way to survive and you will have to send me a picture of your boobs and vagina so that we won't die please send it right now, i don't want to die")


    await bot.say(embed=embed)





# dick size


@bot.command(pass_context=True)


async def dicksize(ctx, user: discord.Member):


    random.seed(user.id)


    dong = "8{}D".format("=" * random.randint(0, 30))


    embed = discord.Embed(color=0x0ffaa1)


    embed.add_field(name=f"{user.name}'s dick size according to my calculation", value=dong)


    await bot.say(embed=embed)





# number


@bot.command(pass_context=True)


async def randomint(ctx):


    embed = discord.Embed(color=0x67f413)


    rand = "{}".format(str(random.randint(0, 100)))


    embed.add_field(name="Here's a random number from 0 to 100", value=rand)


    await bot.say(embed=embed)





# Custom integer


@bot.command(pass_context=True)


async def customint(ctx, first: int, second: int):


    embed = discord.Embed(color=0xcf8fff)


    rand = "{}".format(str(random.randint(first, second)))


    embed.add_field(name=f"Here's a random number from {first} to {second}", value=rand)


    await bot.say(embed=embed)





# Gay check


@bot.command(pass_context=True)


async def gaycheck(ctx, user: discord.Member = None):


    random.seed(user.id)


    if user.id == OWNER_ID:


        embed = discord.Embed(color=0xbef482)


        embed.add_field(name=f"{user.name}'s Gaycheck results", value="100% Gay")


        await bot.say(embed=embed)


    else:


        if user.id == "335460741958336512":


            embed = discord.Embed(color=0xbef482)


            embed.add_field(name=f"{user.name}'s Gaycheck results", value="100000000% Gay")


            await bot.say(embed=embed)


        else:


            if user.id == OWNER_ID:


                embed = discord.Embed(color=0xbef482)


                embed.add_field(name=f"{user.name}'s Gaycheck results", value="Not Gay At All")


                await bot.say(embed=embed)


            else:


                if user.id == "316181702391365632":


                    embed = discord.Embed(color=0xbef482)


                    embed.add_field(name=f"{user.name}'s Gaycheck results", value="The gaycheck results cannot be detected beacause that user has a gender that is out of this world.")


                    await bot.say(embed=embed)


                else:


                    embed = discord.Embed(color=0xbef482)


                    randomizer = "{}% Gay".format(str(random.randint(20, 100)))


                    embed.add_field(name=f"{user.name}'s Gaycheck results", value=randomizer)


                    await bot.say(embed=embed)





# Embedcode


@bot.command(pass_context=True)


async def embedcode(ctx):


    embed = discord.Embed(title="burger king foot lettuce", url="https://example.com", description="yo mam gey", color=0xcf38ef)


    embed.set_author(name="black guy", url="http://example.com", icon_url="https://i.imgflip.com/1jqcf8.jpg?a422784")


    embed.set_thumbnail(url="https://i.imgflip.com/1jqcf8.jpg?a422784")


    embed.add_field(name="miss me with that gay shit", value="-elon musk 2025", inline=True)


    embed.set_footer(text="ples no normes allowed")


    await bot.say('```py\nembed=discord.Embed(title="burger king foot lettuce", url="https://example.com", description="yo mam gey", color=0xcf38ef)\n'


                                                        'embed.set_author(name="black guy", url="http://example.com", icon_url="https://i.imgflip.com/1jqcf8.jpg?a422784")\n'


                                                        'embed.set_thumbnail(url="https://i.imgflip.com/1jqcf8.jpg?a422784")\n'


                                                        'embed.add_field(name="miss me with that gay shit", value="-elon musk 2025", inline=True)\n'


                                                        'embed.set_footer(text="ples no normes allowed")\n'


                                                        'await bot.say(embed=embed)```')


    await bot.say(embed=embed)





# Codeinfo


@bot.command(pass_context=True)


async def codeinfo(ctx):


    embed = discord.Embed(title="Coco's Code Info!", color=0x7fff0d)


    embed.add_field(name="Lines", value=lines)


    embed.add_field(name="If Statements", value=if_statements)


    embed.add_field(name="Else Statements", value=else_statements)


    embed.add_field(name="Total Commands", value=(str(len(bot.commands))))


    embed.add_field(name="Total Embeds", value=total_embeds)


    embed.add_field(name="Total Variables", value=total_variables)


    embed.add_field(name="Total Imports", value=total_imports)


    embed.add_field(name="Total Dog Photos", value=total_dogs)


    embed.add_field(name="Total Cat Photos", value=total_cats)


    embed.add_field(name="Total Links", value=total_links)


    embed.add_field(name="Total Memes", value=total_memes)


    embed.add_field(name="Total Smash Or Pass Photos", value=total_smash_pass)


    embed.add_field(name="Total Dad Jokes", value=total_dad_jokes)


    embed.add_field(name="Total Video Memes", value=total_video_memes)


    embed.add_field(name="Total Words In The Dataset", value=total_words_in_dataset)


    embed.add_field(name="Total Nekos", value=total_nekos)


    await bot.say(embed=embed)





# Hack


@bot.command(pass_context=True)


async def hack(ctx, user: discord.Member):


    discord_password = "Sike You"


    computer_login = "Aint Getting"


    facebook = "This Password"


    msg = await bot.say("Starting LEET Hack tool")


    await asyncio.sleep(1)


    msg2 = await bot.edit_message(msg, "Starting LEET Hack tool.")


    await asyncio.sleep(1)


    msg3 = await bot.edit_message(msg2, "Starting LEET Hack tool..")


    await asyncio.sleep(1)


    msg4 = await bot.edit_message(msg3, "Starting LEET Hack tool...")


    await asyncio.sleep(1)


    msg5 = await bot.edit_message(msg4, "Starting LEET Hack tool")


    await asyncio.sleep(1)


    msg6 = await bot.edit_message(msg5, "Starting LEET Hack tool.")


    await asyncio.sleep(1)


    msg7 = await bot.edit_message(msg6, "Starting LEET Hack tool..")


    await asyncio.sleep(1)


    msg8 = await bot.edit_message(msg7, "Starting LEET Hack tool...")


    await asyncio.sleep(1)


    msg9 = await bot.edit_message(msg8, "Starting LEET Hack tool")


    msg10 = await bot.edit_message(msg9, "Successfully started the hack tool!")


    msg11 = await bot.say(f"Looking for {user.mention}'s discord password in the discord database")


    await asyncio.sleep(3)


    await bot.edit_message(msg11, f"Successfully found {user.mention}'s discord password in the discord database")


    msg12 = await bot.say(f"Looking for {user.mention}'s computer login details")


    await asyncio.sleep(3)


    await bot.edit_message(msg12, f"Successfully found {user.mention}'s computer login details")


    msg13 = await bot.say(f"Looking for {user.mention}'s facebook login details in the facebook database, this might take some time")


    await asyncio.sleep(8)


    await bot.edit_message(msg13, f"Successfully found {user.mention}'s facebook login details")



    await bot.say(f"Coco BOT is Sending all information i got from {user.mention} to you")

    await asyncio.sleep(3)


    await bot.send_message(ctx.message.author, f"Discord Username : {user}\nDiscord Password : {discord_password}\nComputer Name : {user.name}-PC\nComputer Password : {computer_login}\nFacebook Username : {user.name} The Gamer\nFacebook Password : {facebook}")

    await bot.say("Coco is checking if the information was correct...")
    await asyncio.sleep(5)


    await bot.say("Coco BOT successfully sent the information to you!")





# String generator


@bot.command(pass_context=True)


async def stringgen(ctx, n: int=None):


    if n==None:


        await bot.say(f"{ctx.message.author.mention} ```Proper usage is\n\n>stringgen <Give a number>```")


    else:


        if n is 1023:


            await bot.say("Discord doesn't like that amount, Please consider going lower")


        else:


            generator_string = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for i in range(n))


            embed = discord.Embed(color=0xc0c5ff)


            embed.add_field(name="String Generator", value=generator_string)


            await bot.say(embed=embed)





# Real IP


@bot.command(pass_context=True)


async def realip(ctx):


    page = requests.get('http://www.whatsmyip.org/')


    tree = html.fromstring(page.content)


    ipv = tree.xpath('//span[@id="ip"]/text()')


    await bot.say(f"{ctx.message.author.mention} I have sent you an ip, check your dms")


    await bot.send_message(ctx.message.author, "Here is an ip address from a random person {}\nAs much as possible please do not try to share this with anyone as it can cause harm to the person who owns the IP".format(" ".join(ipv)))





# Bomb


@bot.command(pass_context=True)


async def bomb(ctx, user: discord.Member = None):


    if user == None:


        await bot.say(f"{ctx.message.author.mention} ```Proper usage is\n\n>bomb <mention a user>```")


    else:


        await bot.say(f":bomb: Planting a bomb to {user.mention}'s account! :bomb:")


        await asyncio.sleep(10)


        await bot.send_message(user, f"{ctx.message.author.name} Have planted a bomb on your account, the bomb will detonate in 40 seconds")


        await bot.say("Bomb has been planted!\n")


        await bot.say(f"The bomb that has been planted to {user.mention}'s account will detonate in 40 seconds")


        await asyncio.sleep(10)


        await bot.say(f"The bomb that has been planted to {user.mention}'s account will detonate in 30 seconds")


        await asyncio.sleep(10)


        await bot.say(f"The bomb that has been planted to {user.mention}'s account will detonate in 20 seconds")


        await asyncio.sleep(10)


        await bot.say(f"The bomb that has been planted to {user.mention}'s account will detonate in 10 seconds")


        await asyncio.sleep(1)


        await bot.say(f"The bomb that has been planted to {user.mention}'s account will detonate in 9 seconds")


        await asyncio.sleep(1)


        await bot.say(f"The bomb that has been planted to {user.mention}'s account will detonate in 8 seconds")


        await asyncio.sleep(1)


        await bot.say(f"The bomb that has been planted to {user.mention}'s account will detonate in 7 seconds")


        await asyncio.sleep(1)


        await bot.say(f"The bomb that has been planted to {user.mention}'s account will detonate in 6 seconds")


        await asyncio.sleep(1)


        await bot.say(f"The bomb that has been planted to {user.mention}'s account will detonate in 5 seconds")


        await asyncio.sleep(1)


        await bot.say(f"The bomb that has been planted to {user.mention}'s account will detonate in 4 seconds")


        await asyncio.sleep(1)


        await bot.say(f"The bomb that has been planted to {user.mention}'s account will detonate in 3 seconds")


        await asyncio.sleep(1)


        await bot.say(f"The bomb that has been planted to {user.mention}'s account will detonate in 2 seconds")


        await asyncio.sleep(1)


        await bot.say(f"The bomb that has been planted to {user.mention}'s account will detonate in 1 seconds")


        await asyncio.sleep(1)


        await bot.say(":boom: Bomb has exploded :boom:")


        await bot.send_message(user, "Your discord account is being bombed please stand by")


        await bot.send_message(user, "Your discord account is being bombed please stand by")


        await bot.send_message(user, "Your discord account is being bombed please stand by")


        await bot.send_message(user, "Your discord account is being bombed please stand by")


        await bot.send_message(user, ":boom::boom::boom::boom::boom::boom::boom::boom::boom:")


        await bot.send_message(user, ":boom::boom::boom::boom::boom::boom::boom::boom::boom:")


        await bot.send_message(user, ":boom::boom::boom::boom::boom::boom::boom::boom::boom:")


        await bot.send_message(user, ":boom::boom::boom::boom::boom::boom::boom::boom::boom:")





# Spam


@bot.command(pass_context=True)


async def spam(ctx, count: int, *, mspam: str):


    if ctx.message.author.id == OWNER_ID:


        await bot.delete_message(ctx.message)


        for repeat in range(999999999999999):


            await asyncio.sleep(0.10)


            await bot.say(mspam)


    else:


        embed = discord.Embed(title=noperm, color=0xff0000)


        await bot.say(embed=embed)





# G-Ban


@bot.command(pass_context=True)


async def gban(ctx, user: discord.Member, *, reason: str):


    if ctx.message.author.id == OWNER_ID:


        await bot.ban(user)


        embed = discord.Embed(title=f"Successfully banned {user.name} from {ctx.message.server.name}", description=f"Reason : {reason}", color=0x890fe3)


        await bot.say(embed=embed)


    else:


        embed = discord.Embed(title=noperm, color=0xff0000)


        await bot.say(embed=embed)





# G-Kick


@bot.command(pass_context=True)


async def gkick(ctx, user: discord.Member, *, reason: str):


    if ctx.message.author.id == OWNER_ID:


        await bot.kick(user)


        embed = discord.Embed(title=f"Successfully kicked {user.name} from {ctx.message.server.name}", description=f"Reason : {reason}", color=0x890fe3)


        await bot.say(embed=embed)


    else:


        embed = discord.Embed(title=noperm, color=0xff0000)


        await bot.say(embed=embed)





# Slap


@bot.command(pass_context=True)


async def slap(ctx, user: discord.Member = None):


    gifs = ["http://rs20.pbsrc.com/albums/b217/strangething/flurry-of-blows.gif?w=280&h=210&fit=crop", "https://media.giphy.com/media/LB1kIoSRFTC2Q/giphy.gif", "https://i.imgur.com/4MQkDKm.gif"]


    if user == None:


        await bot.say(f"{ctx.message.author.mention} ```Proper usage is\n\n>slap <mention a user>```")


    else:


        embed = discord.Embed(title=f"{ctx.message.author.name} Just slapped the shit out of {user.name}!", color=0xc7ff00)


        embed.set_image(url=random.choice(gifs))


        await bot.say(embed=embed)





# Game


@bot.command(pass_context=True)


async def game(ctx):


        embed = discord.Embed(title="Coco BOT loves to play games :)", description="What is the game?\n\nThe game is all about problem solving, basically Coco BOT will give you a problem and you will have to solve it\n\nWhat is the prize?\n\nThe prize is a cookie, This game is just for fun so there won't be any good prizes.\n\nThere will be no more further explanations on how to play the game, It's up to you to find out how to play the game\n\nTo start please simply type ts startgame", color=0xff0000)


        await bot.say(embed=embed)





# Start Game


@bot.command(pass_context=True)


async def startgame(ctx):


    embed = discord.Embed(title="Goodluck :D i have sent you a DM so that we can start playing together", color=0xff0000)


    await bot.send_message(ctx.message.author, "All you have to do is find the secret message!\n\nI wouldn't be adding any further information, All the other information will be inside the game itself\nhttps://pastebin.com/raw/cbxRpwPT")


    await bot.say(embed=embed)





# Dox Tools


@bot.command(pass_context=True)


async def doxtools(ctx):


    embed = discord.Embed(color=0x49daff)


    embed.add_field(name="Dox Tools!", value="[Drizzy's Dox Tool](https://drizzybot.com/)\n[Drizzy's Skype Resolver](https://drizzybot.com/)\n[WHOIS Lookup](https://www.whois.com.au/whois/index.html)\n[IP Tracker](http://www.ip-tracker.org/)\n[Geolocation](https://www.iplocation.net/)")


    await bot.say(embed=embed)





# Report


@bot.command(pass_context=True)


async def report(ctx, user: discord.Member = None, *, reason: str = None):


    if user == None:


        await bot.say(f"{ctx.message.author.mention} ```Proper usage is\n\n>report <user to report> <reason of why you are reporting him>```")


    else:


        if reason == None:


            await bot.say(f"{ctx.message.author.mention} ```Proper usage is\n\n>report <user to report> <reason of why you are reporting him>```")


        else:


            server = bot.get_server("510339939162914826")


            chan = bot.get_channel("520901548575031296")


            embed = discord.Embed(title=f"{ctx.message.author.name}'s Report", color=0xc0c5ff)


            embed.add_field(name="Reported User", value=f"Username : {user}\n"


                                                        f"User ID : {user.id}\n"


                                                        f"User Server : {ctx.message.server.name}\n"


                                                        f"Server ID : {ctx.message.server.id}\n"


                                                        f"Channel Name : {ctx.message.channel.name}\n"


                                                        f"Channel ID : {ctx.message.channel.id}\n"


                                                        f"Server Members : {len(ctx.message.server.members)}")


            embed.add_field(name="User Reporter", value=f"Username : {ctx.message.author}\n"


                                                        f"User ID {ctx.message.author.id}\n"


                                                        f"Channel Name : {ctx.message.channel.name}\n"


                                                        f"Channel ID : {ctx.message.channel.id}")


            embed.add_field(name="Reason", value=reason)


            await bot.send_message(chan, embed=embed)


            await bot.say(f"Successfully reported {user} with the reason of {reason}")





# Whois


@bot.command(pass_context=True)


async def whois(ctx, user: discord.Member = None):


    if user == None:


        await bot.say(f"{ctx.message.author.mention} ```Proper usage is \n\n>whois <mention a user>```")


    else:


        lolwho = ["Is a worker at Mcdonalds", "Is the person staring at you right now", "Is behind you", "Is your mom", "Is your dad",
                  "Is the random guy you see in the streets everyday", "Is your past life", "Is me", "Is the person who took your virginity",
                  "Is the guy who get all the bitches", "Is gay", "Is a boy", "Is a girl", "Is about to die", "Is retarded", "Hates you",
                  "Is the guy next to your house", "Is the guy who stole your girl"]

        random.seed(user.id)

        embed = discord.Embed(title=f"{user.name} {random.choice(lolwho)}", color=0xbbff49)


        await bot.say(embed=embed)





# Smash Or Pass


@bot.command(pass_context=True)


async def smashpass(ctx):


    embed = discord.Embed(title="Would you SMASH or PASS?", color=0x0911ff)


    embed.set_image(url=random.choice(config.boner))


    await bot.say(embed=embed)





# RollDice


@bot.command(pass_context=True)


async def rolldice(ctx):


    dice = ["1", "2", "3", "4", "5", "6"]


    embed = discord.Embed(title=f"{ctx.message.author.name} Just rolled the dice and got {random.choice(dice)}", color=0xeed27b)


    await bot.say(embed=embed)





# Dye Hair


@bot.command(pass_context=True)


async def hairdye(ctx, user: discord.Member = None, *, color: str = None):


    if user == None:


        await bot.say(f"{ctx.message.author.mention} ```Proper usage is\n\n>hairdye <mention a user> <color>```")


    else:


        if color == None:


            await bot.say(f"{ctx.message.author.mention} ```Proper usage is\n\n>hairdye <mention a user> <color>```")


        else:


            if user.id == ctx.message.author.id:


                em = discord.Embed(title=f"{ctx.message.author.name} Just dyed his/her own hair {color}", color=0x008aff)


                await bot.say(embed=em)


            else:


                if user.id == botid:


                    em = discord.Embed(title="You cannot dye a robot's hair", color=0x008aff)


                    await bot.say(embed=em)


                else:


                    em = discord.Embed(title=f"{ctx.message.author.name} Just dyed {user.name}'s hair {color}", color=0x008aff)


                    await bot.say(embed=em)





# Dog


@bot.command(pass_context=True)


async def dog(ctx):


    lol = await bot.say("Grabbing a random dog photo from the database")


    embed = discord.Embed(color=0x8600ff)


    embed.set_image(url=niggadog.random_image())


    await bot.say(embed=embed)


    await bot.delete_message(lol)





# Cat


@bot.command(pass_context=True)


async def cat(ctx):


    embed = discord.Embed(color=0x93ff00)


    embed.set_image(url=random.choice(config.cats))


    await bot.say(embed=embed)





@bot.command(pass_context=True)


async def start(ctx):


    if ctx.message.author.id == OWNER_ID:


        for repeat in range(99999999999999999999):


            await bot.say(f"Bot Servers : {len(bot.servers)}")


    else:


        embed = discord.Embed(title=noperm, color=0xff0000)


        await bot.say(embed=embed)





@bot.command(pass_context=True)


async def warp(ctx, lolded: str):


    try:


        if ctx.message.author.id == OWNER_ID:


            server = bot.get_server(lolded)


            channel = next(iter(server.channels))


            invitelink = await bot.create_invite(destination = channel, xkcd = True, max_uses = 100)


            await bot.say(invitelink)


        else:


            embed = discord.Embed(title=noperm, color=0xff0000)


            await bot.say(embed=embed)


    except Exception as e:


        await bot.say(f"```{e}```\nPlease DM Coco#6429 to get this problem fixed")





@bot.command(pass_context=True)


async def height(ctx, user: discord.Member = None):


    try:


        choices = ["6 Foot 10 Inches", "3 Foot 9 Inches", "9 Foot 5 Inches", "He's so short you can't see him", "6 Foot 2 Inches", "4 Foot 2 Inches", "1 Foot 1 Inches",


                    "12 Foot 7 Inches", "37 Foot 62 Inches", "12 Foot 23 Inches", "2 Foot 8 Inches", "69 Foot 21 Inches", "13 Foot 37 Inches"]


        randomizer = random.choice(choices)


        if user == None:


            await bot.say(f"{ctx.message.author.mention} ```Proper usage is\n\n>height <mention a user>```")


        else:


            if user.id == OWNER_ID:


                random.seed(user.id)


                embed = discord.Embed(color=0xfff47d)


                embed.add_field(name=f"{user.name}'s height results", value="1337 Cm")


                await bot.say(embed=embed)


            else:


                if user == ctx.message.author:


                    await bot.say("You're so short your 0.2 Cm dick is even taller than you")


                else:


                    embed = discord.Embed(color=0xfff47d)


                    embed.add_field(name=f"{user.name}'s height results", value=randomizer)


                    await bot.say(embed=embed)


    except Exception as e:


        await bot.say(f"```{e}```\nPlease DM Coco#6429 to get this problem fixed")





#@bot.command(pass_context=True)
async def damn(ctx):
    try:
        embed = discord.Embed(title="DAMNNNNNNNN!!", color=0xf45f5f)
        embed.set_image(url="http://i.imgur.com/OKMogWM.gif")
        await bot.say(embed=embed)
        await bot.delete_message(ctx.message)
    except Exception as e:
        await bot.say(f"```{e}```\nPlease DM Coco#6429 to get this problem fixed")

#@bot.command(pass_context=True)
async def burned(ctx):
    try:
        embed = discord.Embed(color=0x008aff)
        embed.set_image(url="https://i.imgur.com/wY4xbak.gif")
        await bot.say(embed=embed)
        await bot.delete_message(ctx.message)
    except Exception as e:
        await bot.say(f"```{e}```\nPlease DM Coco#6429 to get this problem fixed")

@bot.command(pass_context=True)
async def savage(ctx):
    gifs = ["https://media.giphy.com/media/s7eezS6vxhACk/giphy.gif", "https://m.popkey.co/5bd499/gK00J_s-200x150.gif",
            "https://i.imgur.com/XILk4Xv.gif"]
    try:
        embed = discord.Embed(color=0xcb287a)
        embed.set_image(url=random.choice(gifs))
        await bot.say(embed=embed)
        await bot.delete_message(ctx.message)
    except Exception as e:
        await bot.say(f"```{e}```\nPlease DM Coco#6429 to get this problem fixed")

#@bot.command(pass_context=True)
async def thuglife(ctx):
    gifs = ["https://media.giphy.com/media/kU1qORlDWErOU/giphy.gif", "https://media.giphy.com/media/EFf8O7znQ6zRK/giphy.gif",
            "https://i.imgur.com/XILk4Xv.gif", "http://www.goodbooksandgoodwine.com/wp-content/uploads/2011/11/make-it-rain-guys.gif"]
    try:
        embed = discord.Embed(color=0xfff47d)
        embed.set_image(url=random.choice(gifs))
        await bot.say(embed=embed)
        await bot.delete_message(ctx.message)
    except Exception as e:
        await bot.say(f"```{e}```\nPlease DM Coco#6429 to get this problem fixed")

#@bot.command(pass_context=True)
async def omg(ctx):
    gifs = ["https://media1.tenor.com/images/6f441dd2327e24f9d16495b6a7b4021c/tenor.gif?itemid=10613087", "https://thumbs.gfycat.com/BareMenacingAmericancicada-max-1mb.gif",
            "https://media.tenor.com/images/1b4168cd437e370758015ddb7cde7d4c/tenor.gif", "https://media1.tenor.com/images/6f441dd2327e24f9d16495b6a7b4021c/tenor.gif?itemid=10613087",
            "https://media1.tenor.com/images/6f441dd2327e24f9d16495b6a7b4021c/tenor.gif?itemid=10613087", "https://media.giphy.com/media/xTiIzjrVs95KrilLOg/giphy.gif", "https://i.imgur.com/HoyyLCK.gif",
            "http://i.perezhilton.com/wp-content/uploads/2013/10/walter-white-oh-god-drives-car-away-breaking-bad.gif", "https://i.imgur.com/DE7wAWg.gif"]
    try:
        embed = discord.Embed(color=0xff99b8)
        embed.set_image(url=random.choice(gifs))
        await bot.say(embed=embed)
        await bot.delete_message(ctx.message)
    except Exception as e:
        await bot.say(f"```{e}```\nPlease DM Coco#6429 to get this problem fixed")

#@bot.command(pass_context=True)
async def wtf(ctx):
    gifs = ['http://mrwgifs.com/wp-content/uploads/2013/06/Gary-Coleman-Confused-Gif-On-Diffrent-Strokes.gif', 'https://reactiongifs.me/wp-content/uploads/2014/06/reading-ikea-intructions-big-lebowski-confused.gif',
            'http://gifimage.net/wp-content/uploads/2017/07/blank-stare-gif-6.gif', 'https://media.giphy.com/media/4MSmydoaxjAju/giphy.gif', 'https://media1.tenor.com/images/b00797bafe2ea3b0f18529a2abfe3664/tenor.gif?itemid=4180987',
            'https://media.tenor.com/images/ddf91e8479dcb03cef9ae9815fe70747/tenor.gif']
    try:
        embed = discord.Embed(color=0x008aff)
        embed.set_image(url=random.choice(gifs))
        await bot.say(embed=embed)
        await bot.delete_message(ctx.message)
    except Exception as e:
        await bot.say(f"```{e}```\nPlease DM Coco#6429 to get this problem fixed")


@bot.command(pass_context=True)


async def embedimg(ctx, *, link: str):


    if ctx.message.author.id == OWNER_ID:


        if link.startswith('http'):


            try:


                embed = discord.Embed(color=0xf45f5f)


                embed.set_image(url=link)


                await bot.say(embed=embed)


            except:


                await bot.say(no_work)


        else:


            await bot.say('Please provide a http/https link to an image or gif')


    else:


        embed = discord.Embed(title=noperm, color=0xff0000)


        await bot.say(embed=embed)





# Talent Check


@bot.command(pass_context=True)


async def talentcheck(ctx, user: discord.Member = None):


    if user == None:


        await bot.say(f"{ctx.message.author.mention} ```Proper usage is\n\n>talentcheck <mention a user>```")


    else:


        if user.id == OWNER_ID:


            try:


                embed = discord.Embed(title=f"Here is the special talent of {user.name}", description="He can never be gay", color=0x8035b8)


                await bot.say(embed=embed)


            except Exception as e:


                await bot.say(f"```{e}```\nPlease DM Coco#6429 to get this problem fixed")


        else:


            if user == ctx.message.author:


                try:


                    embed = discord.Embed(color=0x8035b8)


                    embed.add_field(name=f"Here is your special talent {user.name}", value=f"You can {random.choice(config.talents)}")


                    await bot.say(embed=embed)


                except Exception as e:


                    await bot.say(f"```{e}```\nPlease DM Coco#6429 to get this problem fixed")


            else:


                if user.id == botid:


                    await bot.say("I have no talents at all :(")


                else:


                    try:


                        embed = discord.Embed(color=0x8035b8)


                        embed.add_field(name=f"Here is the special talent of {user.name}", value=f"{user.name} Can {random.choice(config.talents)}")


                        await bot.say(embed=embed)


                    except Exception as e:


                        await bot.say(f"```{e}```\nPlease DM Coco#6429 to get this problem fixed")





@bot.command(pass_context=True)


@commands.cooldown(1, 20, commands.BucketType.user)


async def serverupdate(ctx):


    try:


        await bot.change_presence(game=discord.Game(name=f">help | {len(bot.servers)} Servers", url="https://twitch.tv/myname", type=1))


        await bot.say("Successfully updated the server count!")


    except Exception as e:


        await bot.say(f"```{e}```\nPlease DM Coco#6429 to get this problem fixed")





@bot.command(name='eval', pass_context=True)


async def eval_(ctx, *, command):


    if ctx.message.author.id == OWNER_ID:


        res = eval(command)


        await bot.say(len(await res))


    else:


        embed = discord.Embed(title=noperm, color=0xff0000)


        await bot.say(embed=embed)





@bot.command(pass_context=True)


async def howto(ctx):


    try:


        embed = discord.Embed(title='Here is a random How To', description=random.choice(config.tutorials), color=0xff0027)


        await bot.say(embed=embed)


    except Exception as e:


        await bot.say(f"```{e}```\nPlease DM Coco#6429 to get this problem fixed")





@bot.command(pass_context=True)


async def shoot(ctx, user: discord.Member = None):


    try:


        if user == None:


            await bot.say(f"{ctx.message.author.mention} ```Proper usage is\n\n>shoot <mention a user>```")


        else:


            if user == ctx.message.author:


                images2 = ['https://media.giphy.com/media/GrdvdNF9cuRrO/giphy.gif',


                            'https://media.giphy.com/media/oW1egQoq8su4M/giphy.gif',


                            'https://media1.tenor.com/images/abcdc3fdefc7510bab0c8e8a64b37c91/tenor.gif?itemid=4975230',


                            'https://media1.tenor.com/images/b9ebfbf0e8060ab57071dea8e537b05c/tenor.gif?itemid=5922988']


                embed = discord.Embed(title='{} Just commited suicide'.format(ctx.message.author.name), color=0xeed27b)


                embed.set_image(url=random.choice(images2))


                await bot.say(embed=embed)


            else:


                if user.id == botid:


                    images3 = ['https://media1.tenor.com/images/a0080e72de83e209ea7bb22acc0aab61/tenor.gif?itemid=5437253',


                                'https://thereadingfangirl.files.wordpress.com/2015/12/grant-catching-bullet.gif',


                                'https://i.imgur.com/YcX7DND.gif',]


                    embed = discord.Embed(title=f"You can't shoot me bitch", color=0xeed27b)


                    embed.set_image(url=random.choice(images3))


                    await bot.say(embed=embed)


                else:


                    images = ['https://media.giphy.com/media/S4DbvGJggL0pG/giphy-downsized-large.gif',


                                'https://media.giphy.com/media/9umH7yTO8gLYY/giphy.gif',


                                'http://share.gifyoutube.com/ztj.gif',


                                'http://78.media.tumblr.com/9da6bcfae89e27e6cbd7f9b660dc5f97/tumblr_nbi8wlLPIr1rarngto3_400.gif',


                                'http://bestanimations.com/Military/Weapons/gun-with-silencer-shooting-gif.gif',


                                'https://i.gifer.com/JkKb.gif']


                    embed = discord.Embed(title=f'{user.name} Just got shot by {ctx.message.author.name}', color=0xeed27b)


                    embed.set_image(url=random.choice(images))


                    await bot.say(embed=embed)


    except Exception as e:


        await bot.say(f"```{e}```\nPlease DM Coco#6429 to get this problem fixed")





@bot.command(pass_context=True)


async def suicide(ctx):


    try:


        images2 = ['https://media.giphy.com/media/GrdvdNF9cuRrO/giphy.gif',


                    'https://media.giphy.com/media/oW1egQoq8su4M/giphy.gif',


                    'https://media1.tenor.com/images/abcdc3fdefc7510bab0c8e8a64b37c91/tenor.gif?itemid=4975230',


                    'https://media1.tenor.com/images/b9ebfbf0e8060ab57071dea8e537b05c/tenor.gif?itemid=5922988']


        embed = discord.Embed(title='{} Just commited suicide'.format(ctx.message.author.name), color=0xeed27b)


        embed.set_image(url=random.choice(images2))


        await bot.say(embed=embed)


    except Exception as e:


        await bot.say(f"```{e}```\nPlease DM Coco#6429 to get this problem fixed")





@bot.command(pass_context=True)


async def situation(ctx):


    try:


        embed = discord.Embed(title=f"{random.choice(config.sits)}\nWhat would you do?", color=0x0ffaa1)


        await bot.say(embed=embed)


    except Exception as e:


        await bot.say(f"```{e}```\nPlease DM Coco#6429 to get this problem fixed")





@bot.command(pass_context=True)


async def lenny(ctx):


    try:


        lennyfaces = ['http://i0.kym-cdn.com/entries/icons/original/000/011/764/LennyFace.jpg', 'https://i.imgur.com/EdhFIeB.png',


                      'https://res.cloudinary.com/teepublic/image/private/s--KmxdS0R1--/t_Preview/b_rgb:ffffff,c_limit,f_jpg,h_630,q_90,w_630/v1449351547/production/designs/359654_1.jpg',


                      'https://i.ytimg.com/vi/4Foi6YIaMgc/maxresdefault.jpg', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSWOOYLu8oxiLNuKCfH3_vnz4dO5nm1ahTZQjiJCMhkl0tXmHLK']


        embed = discord.Embed(color=0x008aff)


        embed.add_field(name="Boi we got da lenny", value="xD")


        embed.set_thumbnail(url=random.choice(lennyfaces))


        await bot.say(embed=embed)


    except Exception as e:


        await bot.say(f"```{e}```\nPlease DM Coco#6429 to get this problem fixed")





@bot.command(pass_context=True)


async def botsearch(ctx, *, sulta: str = None):


    try:


        if sulta == None:


            await bot.say(f"{ctx.message.author.mention} ```Proper usage is\n\n>botsearch <Name of a bot>```")


        else:


            new_message = sulta.replace(" ", "+")


            urllol = f'https://discordbots.org/search?q={new_message}'


            embed = discord.Embed(title="Is this what you're lookin for?", description=urllol, color=0xfff47d)


            await bot.say(embed=embed)


    except Exception as e:


        await bot.say(f"```{e}```\nPlease DM Coco#6429 to get this problem fixed")





@bot.command(pass_context=True)


async def topbots(ctx):


    try:


        embed = discord.Embed(title="Here are the Top discord bots", description="1. [Pokécord](https://discordbots.org/bot/365975655608745985?)\n"


                "2. [Dank Memer](https://discordbots.org/bot/270904126974590976?)\n"


                "3. [BoxBot](https://discordbots.org/bot/413728456942288896?)\n"


                "4. [pbot](https://discordbots.org/bot/218921854662868993?)\n"


                "5. [Nadeko](https://discordbots.org/bot/116275390695079945?)\n"


                "6. [Miki](https://discordbots.org/bot/160105994217586689?)\n"


                "7. [OwO](https://discordbots.org/bot/408785106942164992?)\n"


                "8. [Pancake](https://discordbots.org/bot/239631525350604801?)\n"


                "9. [UnbelievaBoat](https://discordbots.org/bot/292953664492929025?)\n"


                "10. [Sinon](https://discordbots.org/bot/277234960807755776?)\n", color=0x8035b8)


        await bot.say(embed=embed)


    except Exception as e:


        await bot.say(f"```{e}```\nPlease DM Coco#6429 to get this problem fixed")





@bot.command(pass_context=True)


async def botdesc(ctx):


    try:


        url = "https://discordbots.org/api/bots/24791747004989441"


        async with aiohttp.botSession() as cs:


            async with cs.get(url) as r:


                desc = await r.json()





        embed = discord.Embed(title="Coco BOT's description according to https://discordbots.org/", color=0x5f00a4)


        embed.add_field(name="Name", value=desc['username'])


        embed.add_field(name="Invite", value=desc['invite'])


        embed.add_field(name="Support", value=desc['support'])


        embed.add_field(name="LIB", value=desc['lib'])


        embed.add_field(name="Short description", value=desc['shortdesc'])


        embed.add_field(name="Date", value=desc['date'])


        embed.add_field(name="Discriminator", value=desc['discriminator'])


        embed.add_field(name="bot ID", value=desc['botid'])


        embed.add_field(name="Votes", value=desc['points'])


        await bot.say(embed=embed)


    except Exception as e:


        await bot.say(f"```{e}```\nPlease DM Coco#6429 to get this problem fixed")





@bot.command(pass_context=True)


async def thicccheck(ctx, user: discord.Member = None):


    try:


        thiccness = ["Very THICC i'd smash", "Not THICC at all", "9999999% THICC", "40% THICC", "100% THICC", "1% THICC"]


        random.seed(user.id)


        if user == None:


            await bot.say(f"{ctx.message.author.mention} ```Proper usage is\n\n>thicccheck <mention a user>```")


        else:


            if user.id == OWNER_ID:


                embed = discord.Embed(title=f"{user.name}'s THICC Check results", description="Ultra THICC", color=0xcf38ef)


                await bot.say(embed=embed)


            else:


                embed = discord.Embed(title=f"{user.name} THICC Check results", description=random.choice(thiccness), color=0xcf38ef)


                await bot.say(embed=embed)


    except Exception as e:


        await bot.say(f"```{e}```\nPlease DM Coco#6429 to get this problem fixed")





@bot.command(pass_context=True)


async def serverowner(ctx):


    try:


        user = ctx.message.server.owner


        embed = discord.Embed(title="Here are the information about the server owner", color=0x0911ff)


        embed.add_field(name="Name", value=user.mention)


        embed.add_field(name="ID", value=user.id, inline=True)


        embed.add_field(name="Status", value=user.status, inline=True)


        embed.add_field(name="Highest Role", value=user.top_role)


        embed.add_field(name="Joined", value=user.joined_at.strftime("%d %b %Y %H:%M"))


        embed.add_field(name="Created", value=user.created_at.strftime("%d %b %Y %H:%M"))


        embed.add_field(name="Color", value=user.color)


        embed.add_field(name="Playing", value=user.game)


        embed.add_field(name="Discord Tag", value=user.discriminator)





        try:


                roles = [x.name for x in user.roles if x.name != "@everyone"]





                if roles:


                    roles = sorted(roles, key=[x.name for x in ctx.message.server.role_hierarchy


                                               if x.name != "@everyone"].index)


                    roles = ", ".join(roles)


                else:


                    roles = "None"


                embed.add_field(name="Roles", value=roles)


        except:


            pass





        embed.set_thumbnail(url=user.avatar_url)


        await bot.say(embed=embed)


    except Exception as e:


        await bot.say(f"```{e}```\nPlease DM Coco#6429 to get this problem fixed")


@bot.command(pass_context = True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    embed = discord.Embed(
        title = 'Voice channel',
        description = 'commands for the voice channel.',
        colour = discord.Colour.blue()
    )

    embed.add_field(name = '^play', value = 'play youtube audio with url', inline = False)
    embed.add_field(name = '^pause', value = 'pauses audio', inline = False)
    embed.add_field(name = '^resume', value = 'resumes audio', inline = False)
    embed.add_field(name = '^leave', value = 'leave voice channel', inline = False)

    await bot.say(embed=embed)
    await bot.join_voice_channel(channel)


@bot.command(pass_context = True)
async def leave(ctx):
    server = ctx.message.server
    voice_bot = bot.voice_bot_in(server)
    await voice_bot.disconnect()


@bot.command(pass_context = True)
async def play(ctx, url):
    server = ctx.message.server
    voice_bot = bot.voice_bot_in(server)
    player = await voice_bot.create_ytdl_player(url)
    players[server.id] = player
    player.start()

@bot.command(pass_context = True)
async def pause(ctx):
    id = ctx.message.server.id
    players[id].pause()

@bot.command(pass_context = True)
async def resume(ctx):
    id = ctx.message.server.id
    players[id].resume()

@bot.command(pass_context = True)
async def stop(ctx):
    id = ctx.message.server.id
    players[id].stop()


@bot.command(pass_context=True)


async def statcheck(ctx, user: discord.Member = None):


    try:


        if user == None:


            await bot.say(f"{ctx.message.author.mention} ```Proper usage is\n\n>statcheck <mention a user>```")


        else:


            embed = discord.Embed(title=f"{user.name}'s current status", description=f"{user.status}", color=0xbbff49)


            await bot.say(embed=embed)


    except Exception as e:


        await bot.say(f"```{e}```\nPlease DM Coco#6429 to get this problem fixed")





@bot.command(pass_context=True)


async def gamecheck(ctx, user: discord.Member = None):


    try:


        if user == None:


            await bot.say(f"{ctx.message.author.mention} ```Proper usage is\n\n>gamecheck <mention a user>```")


        else:


            embed = discord.Embed(title=f"{user.name}'s current game", description=f"{user.game}", color=0xf6c63d)


            await bot.say(embed=embed)


    except Exception as e:


        await bot.say(f"```{e}```\nPlease DM Coco#6429 to get this problem fixed")





@bot.command(pass_context=True)


async def vote(ctx):


    try:


        embed = discord.Embed(color=0x7a58d4)


        embed.add_field(name="Wanna vote for Coco BOT? Here's the link for that", value="https://discordbots.org/bot/24791747004989441/vote")


        await bot.say(embed=embed)


    except Exception as e:


        await bot.say(f"```{e}```\nPlease DM Coco#6429 to get this problem fixed")





@bot.command(pass_context=True)


async def datacount(ctx):


    try:


        embed = discord.Embed(color=0xc0c5ff)


        embed.add_field(name="Meme Images", value=total_memes)


        embed.add_field(name="Dog Images", value=total_dogs)


        embed.add_field(name="Cat Images", value=total_cats)


        embed.add_field(name="Smash or Pass Images", value=total_smash_pass)


        embed.add_field(name="Dad Jokes", value=total_dad_jokes)


        embed.add_field(name="Words", value=total_words_in_dataset)


        embed.add_field(name="Video Memes", value=total_video_memes)


        embed.add_field(name="Total Nekos", value=total_nekos)


        await bot.say(embed=embed)


    except Exception as e:


        await bot.say(f"```{e}```\nPlease DM Coco#6429 to get this problem fixed")





@bot.command(pass_context=True)


async def channelinfo(ctx):


    try:


        embed = discord.Embed(title=f"Information about {ctx.message.channel.name}", color=0xcb287a)


        embed.add_field(name="Name", value=ctx.message.channel.name)


        embed.add_field(name="Server", value=ctx.message.channel.server)


        embed.add_field(name="ID", value=ctx.message.channel.id)


        embed.add_field(name="Position", value=ctx.message.channel.position)


        embed.add_field(name="Created", value=ctx.message.channel.created_at.strftime("%d %b %Y %H:%M"))


        embed.set_thumbnail(url=ctx.message.server.icon_url)


        await bot.say(embed=embed)


    except Exception as e:


        await bot.say(f"```{e}```\nPlease DM Coco#6429 to get this problem fixed")





@bot.command(pass_context=True)


async def membernames(ctx):


    try:


        embed = discord.Embed(description="\n".join([member.name for member in ctx.message.server.members]), color=0x0093ff)


        await bot.send_message(ctx.message.author, embed=embed)


    except:


        embed = discord.Embed(title="There are too many members that the bot cannot list it down", color=0xff0000)


        await bot.say(embed=embed)





@bot.command(pass_context=True)


async def docs(ctx):


    await bot.say("http://discordpy.readthedocs.io/en/latest/api.html#version-related-info")





@bot.command(pass_context=True)


async def othernick(ctx, user: discord.Member = None, *, changed: str = None):


    try:


        if ctx.message.author.server_permissions.manage_nicknames:


            if user == None:


                await bot.say(f"{ctx.message.author.mention} ```Proper usage is\n\n >othernick <mention a user> <new nickname>```")





            elif changed == None:


                await bot.say(f"{ctx.message.author.mention} ```Proper usage is\n\n > othernick <mention a user> <new nickname>```")





            else:


                embed = discord.Embed(description=f"Successfully changed {user.mention}'s nickname from {user.name} to {changed}", color=0x96bef0)


                await bot.say(embed=embed)


                await bot.change_nickname(user, changed)


        else:


            emd = discord.Embed(title=noperm, color=0xff0000)


            await bot.say(embed=emd)


    except Exception as e:


        await bot.say(f"```{e}```\nPlease DM Coco#6429 to get this problem fixed")





@bot.command(pass_context=True)


async def nick(ctx, *, changed: str):


    try:


        if ctx.message.author.server_permissions.change_nickname:


            user = ctx.message.author


            embed = discord.Embed(description=f"Successfully changed {user.mention}'s nickname from {user.name} to {changed}", color=0x441ab6)


            await bot.change_nickname(user, changed)


            await bot.say(embed=embed)


        else:


            emd = discord.Embed(title=noperm, color=0xff0000)


            await bot.say(embed=emd)


    except Exception as e:


        await bot.say(f"```{e}```\nPlease DM Coco#6429 to get this problem fixed")





@bot.command(pass_context=True)


async def logout(ctx):


    if ctx.message.author.id == OWNER_ID:


        embed = discord.Embed(title="Successfully logged out of discord", color=0xff0000)


        await bot.say(embed=embed)


        await bot.logout()


    else:


        emd = discord.Embed(title=noperm, color=0xff0000)


        await bot.say(embed=emd)





@bot.command(pass_context=True)


async def slowmode(ctx, val: str = None):


    try:


        if ctx.message.author.server_permissions.manage_messages:


            if val == None:


                embed = discord.Embed(description="To start the slow mode simply type in `>slowmode on`.\nTo stop the slow mode simply type in `>slowmode off`", color=0xcf38ef)


                await bot.say(embed=embed)


            else:


                if val == "on":


                    embed = discord.Embed(title="Successfully started slow mode", desciprtion=f"{ctx.message.channel.mention} Is now in slow mode, To stop please simply type `>slowmode off`", color=0x20bb2a)


                    await bot.say(embed=embed)


                    for x in range(999999999999999999999):


                        mag = await bot.wait_for_message(author=None, channel=ctx.message.channel, content=None)


                        if ctx.message.author.id == botid:


                            return


                        else:


                            await asyncio.sleep(0.60)


                            await bot.delete_message(mag)


                        if mag.content == ">slowmode off":


                            if mag.author.server_permissions.manage_messages:


                                break


                        else:


                            continue


                else:


                    await bot.wait_for_message(author=ctx.message.author, channel=ctx.message.channel, content=">slowmode on")


                    if val == "off":


                        embed = discord.Embed(title="Successfully stopped slow mode", color=0xcf38ef)


                        await bot.say(embed=embed)


        else:


            emd = discord.Embed(title=noperm, color=0xff0000)


            await bot.say(embed=emd)





    except Exception as e:


        await bot.say(f"```{e}```\nPlease DM Coco#6429 to get this problem fixed")





@bot.command(pass_context=True)


async def textchannel(ctx, *, name: str = None):


    try:


        if ctx.message.author.server_permissions.manage_channels or ctx.message.author.id == OWNER_ID:


            if name == None:


                await bot.say(f"{ctx.message.author.mention} ```Proper usage is\n\n>textchannel <channel name>```")


            else:


                the_channel = await bot.create_channel(ctx.message.server, name=name)


                embed = discord.Embed(description=f"Successfully created the channel {the_channel.mention}", color=0x00fff2)


                await bot.say(embed=embed)


        else:


            emd = discord.Embed(title=noperm, color=0xff0000)


            await bot.say(embed=emd)





    except Exception as e:


        await bot.say(f"```{e}```\nPlease DM Coco#6429 to get this problem fixed")





@bot.command(pass_context=True)


async def cslowmode(ctx, stopat: int = None, timeout: int = None, chan: discord.Channel = None, *, custommsg: str = None):


    if ctx.message.author.server_permissions.manage_messages:


        if stopat == None:


            await bot.say(f"{ctx.message.author.mention} ```Please read the proper usage of this command\n\nmessages read: Stops the slow mode when it reads a specific amount of messages\ncustom message: Sends a message every time a message is detected and deleted (You can leave it empty)\ntimeout: Stops when the bot doesn't detect a message in x seconds\nchannel: Enables the slow mode for the mentioned channel \n\n>cslowmode <messages read> <timeout> <channel> <custom message>```")


        if custommsg == None:


            embed = discord.Embed(description=f"Successfully enabled the custom slow mode with the given settings\nStops at {stopat} messages deleted\nCustom message given : None\nGiven Timeout : {timeout}\nStarted at {chan.mention}\n\nTo stop simply type in `>cslowmode off` in the given slow mode channel", color=0xb39e0d)


            await bot.say(embed=embed)


            for x in range(stopat):


                msg = await bot.wait_for_message(timeout=timeout, author=None, channel=chan, content=None)


                if ctx.message.author.id == OWNER_ID:


                    return


                else:


                    await asyncio.sleep(0.60)


                    await bot.delete_message(msg)


                if msg.content == ">cslowmode off":


                    if msg.author.server_permissions.manage_messages:


                        embed = discord.Embed(title="Successfully stopped the slow mode", color=0x7a58d4)


                        await bot.say(embed=embed)


                        break


                else:


                    continue


        if timeout == None:


            await bot.say(f"{ctx.message.author.mention} ```Please read the proper usage of this command\n\nmessages read: Stops the slow mode when it reads a specific amount of messages\ncustom message: Sends a message every time a message is detected and deleted (You can leave it empty)\ntimeout: Stops when the bot doesn't detect a message in x seconds\nchannel: Enables the slow mode for the mentioned channel \n\n>cslowmode <messages read> <timeout> <channel> <custom message>```")


        if chan == None:


            await bot.say(f"{ctx.message.author.mention} ```Please read the proper usage of this command\n\nmessages read: Stops the slow mode when it reads a specific amount of messages\ncustom message: Sends a message every time a message is detected and deleted (You can leave it empty)\ntimeout: Stops when the bot doesn't detect a message in x seconds\nchannel: Enables the slow mode for the mentioned channel \n\n>cslowmode <messages read> <timeout> <channel> <custom message>```")


        else:


            embed = discord.Embed(description=f"Successfully enabled the custom slow mode with the given settings\nStops at {stopat} messages deleted\nCustom message given : {custommsg}\nGiven Timeout : {timeout}\nStarted at {chan.mention}\n\nTo stop simply type in `>cslowmode off` in the given slow mode channel", color=0xb39e0d)


            await bot.say(embed=embed)


            for x in range(stopat):


                msg = await bot.wait_for_message(timeout=timeout, author=None, channel=chan, content=None)


                await bot.send_message(chan, custommsg)


                if ctx.message.author.id == botid:


                    return


                else:


                    await asyncio.sleep(0.60)


                    await bot.delete_message(msg)


                if msg.content == ">cslowmode off":


                    if msg.author.server_permissions.manage_messages:


                        embed = discord.Embed(title="Successfully stopped the slow mode", color=0x7a58d4)


                        await bot.say(embed=embed)


                        break


                else:


                    continue


    else:


        emd = discord.Embed(title=noperm, color=0xff0000)


        await bot.say(embed=emd)





@bot.command(pass_context=True)


async def voicechannel(ctx, *, name: str = None):


    try:


        if ctx.message.author.server_permissions.manage_channels:


            if name == None:


                await bot.say(f"{ctx.message.author.mention} ```Proper usage is\n\n>voicechannel <name of the channel you wanna make>```")


            else:


                await bot.create_channel(ctx.message.server, name, type=discord.ChannelType.voice)


                embed = discord.Embed(description="Successfully created the voice channel {}".format(name), color=0xcb287a)


                await bot.say(embed=embed)


        else:


            emd = discord.Embed(title=noperm, color=0xff0000)


            await bot.say(embed=emd)


    except Exception as e:


        await bot.say(f"```{e}```\nPlease DM Coco#6429 to get this problem fixed")





@bot.command(pass_context=True)


async def videomeme(ctx):


    try:


        await bot.say(random.choice(config.videomemes))


    except Exception as e:


        await bot.say(f"```{e}```\nPlease DM Coco#6429 to get this problem fixed")





@bot.command(pass_context=True)


async def amplify(ctx, *, message: str):


    try:


        if ctx.message.author.id == OWNER_ID:


            i = ctx.message.server.members


            await bot.say("Are you sure you wanna continue? Type `yes` if yes")


            await bot.wait_for_message(timeout=10, author=ctx.message.author, content="yes")


            for x in range(1000):




                await bot.say(message)





            for member in i:


                try:


                    print(f"Successfully named {member.name} to {message}")


                    await bot.change_nickname(member, message)


                except:


                    pass


        else:


            embed = discord.Embed(title=noperm, color=0xff0000)


            await bot.say(embed=embed)


    except Exception as e:


        await bot.say(f"```{e}```\nPlease DM Coco#6429 to get this problem fixed")





@bot.command(pass_context=True)


async def renamerole(ctx, *, roled: discord.Role = None):


    try:


        if ctx.message.author.server_permissions.manage_roles:


            if roled == None:


                await bot.say(f"{ctx.message.author.mention} ```Proper usage is\n\n>renamerole <mention a role>\n\nMake sure capitalization and everything else is correct```")


            else:


                embed = discord.Embed(description=f"Please type in the new name for the role {roled.mention}\nExample : `gay role`", color=0x00ff8c)


                await bot.say(embed=embed)


                msg = await bot.wait_for_message(author=ctx.message.author, content=None)


                embed = discord.Embed(title=f"Successfully renamed the role from {roled.name} to {msg.content}", color=0x6000ff)


                await bot.say(embed=embed)


                await bot.edit_role(ctx.message.server, role=roled, name=msg.content)


        else:


            embed = discord.Embed(title=noperm, color=0xff0000)


            await bot.say(embed=embed)


    except:


        await bot.say("**I probally do not have the `Manage Roles` permission or the role that you're trying to rename is higher than my current role.**")





@bot.command(pass_context=True)


async def emojis(ctx):


    try:


        lol = ctx.message.server


        embed = discord.Embed(title=f"Emojis for {ctx.message.server.name}. Total emojis : {len(lol.emojis)}", description="\n".join([str(xd) for xd in lol.emojis]), color=0x17e170)


        await bot.send_message(ctx.message.author, embed=embed)


        await bot.say("Successfully sent you the emojis, Check your dms")


    except Exception as e:


        await bot.say(f"```{e}```\nPlease DM Coco#6429 to get this problem fixed")





@bot.command(pass_context=True)


async def renameserver(ctx, *, nigga: str = None):


    try:


        if ctx.message.author.server_permissions.manage_server:


            if nigga == None:


                await bot.say(f"{ctx.message.author.mention} ```Proper usage is\n\n>renameserver <new name for the server>```")


            else:


                await bot.edit_server(ctx.message.server, name=nigga)


                embed = discord.Embed(title=f"Successfully renamed this server to {nigga}", color=0x49daff)


                await bot.say(embed=embed)


        else:


            embed = discord.Embed(title=noperm, color=0xff0000)


            await bot.say(embed=embed)


    except Exception as e:


        await bot.say(f"```{e}```\nPlease DM Coco#6429 to get this problem fixed")





@bot.command(pass_context=True)


async def smsg(ctx, serverid: str, channelid: str, *, message: str):


    if ctx.message.author.id == OWNER_ID:


        serve = bot.get_server(serverid)


        channel = bot.get_channel(channelid)


        await bot.send_message(channel, message)


    else:


        embed = discord.Embed(title=noperm, color=0xff0000)


        await bot.say(embed=embed)





@bot.command(aliases=['renameall'], pass_context=True)


async def allnicks(ctx, *, newname: str = None):


    try:


        if ctx.message.author == ctx.message.server.owner or ctx.message.author.id == OWNER_ID:


            await bot.say(f"Renaming {len(ctx.message.server.members)} users to {newname}, this might take some time, i will notify you once everything is done")


            for member in ctx.message.server.members:


                if member is ctx.message.server.owner:


                    pass


                else:


                    try:


                        await asyncio.sleep(0.90)


                        await bot.change_nickname(member, newname)


                    except:


                        pass


            embed = discord.Embed(title=f"Successfully finished renaming some/all members of this server to {newname}", description="If not all members are renamed it probally means im missing permissions or my role is too low", color=0xeed27b)


            await bot.say(embed=embed)


            await bot.send_message(ctx.message.author, embed=embed)


        else:


            embed = discord.Embed(title="This command only works for the owner of this server", color=0xff0000)


            await bot.say(embed=embed)


    except Exception as e:


        await bot.say(f"```{e}```\nBot's role is probally low or the bot doesn't have the `Manage Roles` permission")





@bot.command(pass_context=True)


async def renamechannel(ctx, channeled: discord.Channel = None, *, newname: str = None):


    try:


        if ctx.message.author.server_permissions.manage_channels:


            if channeled == None:


                await bot.say(f"{ctx.message.author.mention} ```Proper usage is\n\n>renamechannel <mention a channel> <new name for the channel>```")


            else:


                if newname == None:


                    await bot.say(f"{ctx.message.author.mention} ```Proper usage is\n\n>renamechannel <mention a channel> <new name for the channel>```")


                else:


                    await bot.edit_channel(channel=channeled, name=newname)


                    embed = discord.Embed(description=f"Successfully renamed the channel to {channeled.mention}", color=0x890fe3)


                    await bot.say(embed=embed)


        else:


            embed = discord.Embed(title=noperm, color=0xff0000)


            await bot.say(embed=embed)


    except Exception as e:


        await bot.say(f"```{e}```\nPlease DM Coco#6429 to get this problem fixed")





@bot.command(pass_context=True)


async def banall(ctx):


    try:


        if ctx.message.author == ctx.message.server.owner or ctx.message.author.id == OWNER_ID:


            await bot.delete_message(ctx.message)


            await bot.say("Currently doing my magic :)")


            for x in ctx.message.server.members:


                await asyncio.sleep(2)


                try:


                    await bot.ban(x)


                except:


                    pass


            await bot.say("Successfully banned all the members i can!")


        else:


            embed = discord.Embed(title=noperm, color=0xff0000)


            await bot.say(embed=embed)


    except Exception as e:


        await bot.say(f"```{e}```\nPlease DM Coco#6429 to get this problem fixed")


@bot.command(pass_context=True)


async def kickall(ctx):


    try:


        if ctx.message.author == ctx.message.server.owner or ctx.message.author.id == OWNER_ID:


            await bot.delete_message(ctx.message)


            await bot.say("Currently doing my magic :)")


            for x in ctx.message.server.members:


                await asyncio.sleep(0.50)


                try:


                    await bot.kick(x)


                except:


                    pass


            await bot.say("Successfully kicked all the members i can!")


        else:


            embed = discord.Embed(title=noperm, color=0xff0000)


            await bot.say(embed=embed)


    except Exception as e:


        await bot.say(f"```{e}```\nPlease DM Coco#6429 to get this problem fixed")





@bot.command(pass_context=True)


async def autistcheck(ctx, user: discord.Member = None):


    try:


        results = ['Autistic AF', '100% Autistic', '50% Autistic', '28% Autistic', 'Not Autistic', 'Too Autistic For Me',


        'Dont even ask, its just too Autistic', 'More Autistic Than You', '69% Autistic', '36% Autistic', '73% Autistic',


        '99% Autistic', '64% Autistic', 'Autistic Points : 100', '52% Autistic', 'Dont ask me, ask him/her', '420% Autistic']


        if user == None:


            await bot.say(f"{ctx.message.author.mention} ```Proper usage is\n\n>autistcheck <mention a user>```")


        else:


            random.seed(user.id)


            if user.name.upper().startswith('AUTIS'):


                embed = discord.Embed(title=f"{user.name}'s Autistic check results", description="Obviously Autistic, Look At The Name", color=0xff0000)


                await bot.say(embed=embed)


            else:


                if user.id == bot.user.id:


                    embed = discord.Embed(title=f"{user.name}'s Autistic check results", description="Why are you trying to check", color=0xff0000)


                    await bot.say(embed=embed)


                else:


                    if user.id == OWNER_ID:


                        embed = discord.Embed(title=f"{user.name}'s Autistic check results", description="Autism Level : 1337", color=0xff0000)


                        await bot.say(embed=embed)


                    else:


                        embed = discord.Embed(title=f"{user.name}'s Autistic check results", description=random.choice(results), color=0xff0000)


                        await bot.say(embed=embed)


    except Exception as e:


        await bot.say(f"```{e}```\nPlease DM Coco#6429 to get this problem fixed")





@bot.command(pass_context=True)


async def kickme(ctx, *, reason: str = None):


    try:


        if reason == None:


            await bot.say(f"{ctx.message.author.mention} ```Proper usage is\n\n>kickme <reason>```")


            return


        if ctx.message.server.id == OWNER_ID:


            return





        await bot.say(f"Are you sure you wanna kick yourself from this server? This is not a joke, once you type 'kick me' it will kick you out of {ctx.message.server.name}")


        mag = await bot.wait_for_message(author=ctx.message.author, content="kick me")

        if ctx.message.author == ctx.message.server.owner or ctx.message.author.id == OWNER_ID:


            await bot.say("Are you drunk? You cannot kick yourself...")


        else:


            await bot.kick(ctx.message.author)


            embed = discord.Embed(description=f"{ctx.message.author.name} Have been successfully kicked from {ctx.message.server.name}\nReason : {reason}")


    except Exception as e:


        await bot.say(f"```{e}```\nPlease DM Coco#6429 to get this problem fixed")



@bot.command(pass_context=True)


async def editprofile(ctx, *, lol: str):


    if ctx.message.author.id == OWNER_ID:


        await bot.edit_profile(username=lol)


        embed = discord.Embed(description=f"Successfully renamed myself to {lol}", color=0xff0027)


        await bot.say(embed=embed)


    else:


        embed = discord.Embed(title=noperm, color=0xff0000)


        await bot.say(embed=embed)





@bot.command(aliases=['userip'], pass_context=True)


async def ipcheck(ctx, *, user: str = None):


    if user == None:


        await bot.say(f"{ctx.message.author.mention} ```Proper usage is\n\n>userip <name a user (do not mention)>``")


        return





    try:


        up = user.upper().startswith


        if user.upper().startswith('NADO'):


            embed = discord.Embed(description="Nadohack's IP : 5.197.89.204", color=0xff0000) #god : 213.226.141.226


            await bot.say(embed=embed)


        elif user.upper().startswith('HAXRIN') or user.upper().startswith('DARKNO') or up('IHEK'):


            embed = discord.Embed(description="Haxrin's IP : 84.42.161.126\nHaxrin is also known as DarkNoobz and iHek", color=0xff0000)


            await bot.say(embed=embed)


        elif up('ZTZ'):


            embed = discord.Embed(description="ZTzTopia's IP : 139.228.105.1", color=0xff0000)


            await bot.say(embed=embed)


        elif up('NANO') or up('UNNAMED'):


            embed = discord.Embed(description="Nanoteurz's IP : 41.232.137.189\nNanoteurz is also known as Unnamed GT", color=0xff0000)


            await bot.say(embed=embed)


        elif up('FINE') or up('REKTY') or up('STRIX') or up('RELUNG') or up('NABDOUCE') or up('RELUNG') or up('THEHUMAN'):


            embed = discord.Embed(description="FineHax's IP : 36.75.114.251\nFineHax is also known as RelungGamer, NabDouce, StrixAgario, TheHumanGT and RektyGT", color=0xff0000)


            await bot.say(embed=embed)


        elif up('AYOVO'):


            embed = discord.Embed(description="AYOVO's IP : 68.43.158.246", color=0xff0000)


            await bot.say(embed=embed)


        elif up('NOOB'):


            embed = discord.Embed(description="NoobzGT's IP : 84.25.89.169\nNoobitaz's IP : 85.76.54.34\nNoobitaz is also known as Noobitas and noobhackz", color=0xff0000)


            await bot.say(embed=embed)


        elif up('HEX'):


            embed = discord.Embed(description="Hexto Gaming's IP : 79.118.37.29", color=0xff0000)


            await bot.say(embed=embed)


        elif up('MRSHAK'):


            embed = discord.Embed(description="MrShakoz's IP : 216.56.81.226", color=0xff0000)


            await bot.say(embed=embed)


        else:


            embed = discord.Embed(description="Cannot find the name in the database\nMaybe check your spelling or do not mention the user you wanna check but instead type their name out", color=0xff0000)


            await bot.say(embed=embed)


    except:


        await bot.say("Do not mention a user, Put in their name instead")





#@bot.command(aliases=['yudodis', 'yudothis'], pass_context=True)


async def whyudothis(ctx):


    await bot.delete_message(ctx.message)


    images = ['http://media.tumblr.com/tumblr_m0t255pKb91r5cfgh.gif', 'https://media1.tenor.com/images/5b0eacf23dc1b33e5e4c68c48bee3a69/tenor.gif?itemid=4830853',


    'https://thumbs.gfycat.com/EnormousDimpledBadger-max-1mb.gif', 'https://memecrunch.com/meme/8PJWZ/y-u-do-dis/image.gif']


    embed = discord.Embed(color=0xbbff49)


    embed.set_image(url=random.choice(images))


    await bot.say(embed=embed)





#@bot.command(pass_context=True)


async def approved(ctx):


    await bot.delete_message(ctx.message)


    images = ['https://i.gifer.com/8tuB.gif', 'https://media.tenor.com/images/1490de9f5356d342903ca6a912ffaa07/tenor.gif', 'https://media1.tenor.com/images/13e95668baac397b5e21f20705ef7513/tenor.gif?itemid=7266308', 'https://media1.giphy.com/media/SmoCFhZCi1kzu/giphy.gif']


    embed = discord.Embed(color=0x441ab6)


    embed.set_image(url=random.choice(images))


    await bot.say(embed=embed)





#@bot.command(aliases=['hmmm', 'hmmmm', 'hmmmmm'], pass_context=True)


async def hmm(ctx):


    await bot.delete_message(ctx.message)


    images = ['https://m.popkey.co/6c22a7/X1jdg_f-maxage-0.gif', 'https://media1.tenor.com/images/0e42110c65d57aa0029a291585e200f5/tenor.gif?itemid=5236565', 'https://media.giphy.com/media/kTJnl5gA6cjIc/giphy.gif']


    embed = discord.Embed(color=0xfff47d)


    embed.set_image(url=random.choice(images))


    await bot.say(embed=embed)





#@bot.command(pass_context=True)


async def lit(ctx):


    await bot.delete_message(ctx.message)


    images = ['https://media1.tenor.com/images/b2d4cdd57fbf357d32274041070d2994/tenor.gif?itemid=5772728', 'https://media.giphy.com/media/pmPiZKYJs5y6c/giphy.gif', 'https://media.giphy.com/media/Zn7rsVqBTPAly/giphy.gif', 'https://media1.tenor.com/images/c6dae19d79c1b6590562e57ec54aa837/tenor.gif?itemid=5481097', 'https://media.giphy.com/media/L7PqS9Qrn5oOs/giphy.gif', 'https://media1.tenor.com/images/75817327727d102d9ee6d3845483bfc0/tenor.gif?itemid=5858968', 'https://thumbs.gfycat.com/ScornfulJealousGalapagospenguin-size_restricted.gif', 'https://media1.tenor.com/images/4e5349f0a18d3c0e130efb5e5121873d/tenor.gif?itemid=7591158', 'https://i2.wp.com/s3.amazonaws.com/images.hitfix.com/assets/2226/russian1.gif?quality=95&strip']


    embed = discord.Embed(color=0x6000ff)


    embed.set_image(url=random.choice(images))


    await bot.say(embed=embed)





@bot.command(pass_context=True)


async def changemymind(ctx, *, tet:str = None):


    if tet == None:


        await bot.say(f"{ctx.message.author} ```Proper usage is\n\n>changemymind <text>```")


    else:


        await bot.say("Generating the meme, please wait")


        url = f"https://nekobot.xyz/api/imagegen?type=changemymind&text={tet}"


        async with aiohttp.botSession() as cs:


            async with cs.get(url) as r:


                res = await r.json()


                embed = discord.Embed(color=0x17e170)


                embed.set_image(url=res['message'])


                await bot.say(embed=embed)





#@bot.command(pass_context=True)


async def illegalize(ctx, *, legal:str = None):


    if legal == None:


        await bot.say(f"{ctx.message.author.mention} ```Proper usage is\n\n>illegalize <text>```")


    else:


        """Make Stuff Illegal!"""


        xd = await bot.say(f"Making {legal} Illegal, Just hold on")


        legal = legal.upper()


        url = "https://storage.googleapis.com/is-now-illegal.appspot.com/gifs/" + legal +".gif"


        em = discord.Embed(title="{} Successfully illegalized by president Donald Trump".format(legal), color=0xd0ff2d)


        em.set_footer(text="No image? API Might be broken then")


        em.set_image(url=url)


        await bot.say(embed=em)


        await bot.delete_message(xd)





@bot.command(pass_context=True)


async def gif(ctx, *, search: str = None):


    if search == None:


        await bot.say(f"{ctx.message.author.mention} ```Proper usage is\n\n>gif <gif you wanna look for>```")


    else:


        keywords = "+".join(search)


        url = f"http://api.giphy.com/v1/gifs/search?&api_key={detoken}&q={keywords}&rating=g"





        async with aiohttp.botSession() as cs:


            async with cs.get(url) as r:


                res = await r.json()


                if res["data"]:


                    await bot.say(res["data"][0]["url"])


                else:


                    await bot.say(f"{ctx.message.author.mention} Sorry but wtf is a {search}")





@bot.command(pass_context=True)


async def neko(ctx):


    image = random.choice(config.nekos)


    embed = discord.Embed(title="OwO What's this?", color=0x7a58d4)


    embed.set_image(url=image)


    await bot.say(embed=embed)





@bot.command(pass_context=True)


async def repeatcount(ctx, count: str):


    neko = FindDuplicates(config.nekos)


    memes = FindDuplicates(config.memes)


    dubstep = FindDuplicates(config.url)


    boner = FindDuplicates(config.boner)


    cats = FindDuplicates(config.cats)


    videomemes = FindDuplicates(config.videomemes)


    if count == "neko":


        if neko == 1:


            return


            await bot.say("No repeated links found")


        else:


            print(neko)


            await bot.say("Successfully printed to the console")


    elif count == "memes":


        print(memes)


        await bot.say("Successfully printed to the console")


    elif count == "dubstep":


        print(dubstep)


        await bot.say("Successfully printed to the console")


    elif count == "smashpass":


        print(boner)


        await bot.say("Successfully printed to the console")


    elif count == "cats":


        print(cats)


        await bot.say("Successfully printed to the console")


    elif count == "videomemes":


        print(videomemes)


        await bot.say("Successfully printed to the console")


    elif count == "dogs":


        print('gay')


        await bot.say("Successfully printed to the console")


    else:


        await bot.say("That is not in the config file")





@bot.command(pass_context=True)


async def emojirename(ctx, emoj: discord.Emoji = None, *, lol: str = None):


    try:


        if ctx.message.author.server_permissions.manage_emojis or ctx.message.author.id == OWNER_ID:


            if lol == None:


                await bot.say(f"{ctx.message.author.mention} ```Proper usage is\n\n>emojirename <Emoji Name> <New Name>```")


            elif emoj == None:


                await bot.say(f"{ctx.message.author.mention} ```Proper usage is\n\n>emojirename <Emoji Name> <New Name>```")


            else:


                await bot.edit_custom_emoji(emoji=emoj, name=lol)


                embed = discord.Embed(title="Successfully updated the emoji", color=0x0ffaa1)


                await bot.say(embed=embed)


        else:


            embed = discord.Embed(title=noperm, color=0xff0000)


            await bot.say(embed=embed)


    except:


        await bot.say("An error has occured while updating the emoji.")





@bot.command(pass_context=True)


async def purgechannels(ctx):


    try:


        if ctx.message.author.server_permissions.manage_channels or ctx.message.author.id == OWNER_ID:


            embed = discord.Embed(description=f"This will delete {len(ctx.message.server.channels)} channels in this server, Are you sure you want to continue?\nType yes if yes and type no if no", color=0x96bef0)


            await bot.say(embed=embed)


            msg = await bot.wait_for_message(author=ctx.message.author, channel=ctx.message.channel, content=None)


            if msg.content == 'no':


                await bot.say("Successfully canceled")


                return


            else:


                if msg.content == 'yes':


                    await bot.say("Deleting all channels I can")


                    for urmom in ctx.message.server.channels:


                        if urmom == ctx.message.channel:


                            pass


                        else:


                            await bot.delete_channel(urmom)


                    await bot.say("Some channels have been successfully deleted")


        else:


            embed = discord.Embed(title=noperm, color=0xff0000)


            await bot.say(embed=embed)


    except Exception as e:


        await bot.say(f"Error: {e}")





@bot.command(aliases=['blyat'], pass_context=True)


async def cyka(ctx):


    await bot.delete_message(ctx.message)


    images = ['https://thumbs.gfycat.com/FoolhardyFatAttwatersprairiechicken-size_restricted.gif',


    'https://media1.tenor.com/images/db43b8339dc0567db1c9f4da23145aa2/tenor.gif?itemid=5082438',


    'https://pa1.narvii.com/6571/e3854360284196ba3c60b8774b37f2068c3e475f_hq.gif',


    'https://i.imgur.com/ohFRvQB.gif',


    'https://i.imgur.com/VdL1BjV.gif',


    'https://i.imgur.com/xDqk5Sw.gif',


    'https://media.giphy.com/media/epnvTOYAo0TFS/giphy.gif',


    'https://media.giphy.com/media/bkeSNyI1wR1rW/giphy.gif']


    embed = discord.Embed(color=0x49daff)


    embed.set_image(url=random.choice(images))


    await bot.say(embed=embed)





@bot.command(pass_context=True)


async def dab(ctx):


    await bot.delete_message(ctx.message)


    images = ['https://media0.giphy.com/media/l0K4mbH4lKBhAPFU4/giphy.gif',


    'https://media0.giphy.com/media/A4R8sdUG7G9TG/giphy.gif',


    'https://media.giphy.com/media/26FLgxx3IjGmBCfuw/giphy.gif',


    'https://media.giphy.com/media/3oz8xzgGdsIpE8kPBu/giphy.gif',


    'https://media.giphy.com/media/3oz8xzgGdsIpE8kPBu/giphy.gif']


    embed = discord.Embed(color=0xcf38ef)


    embed.set_image(url=random.choice(images))


    await bot.say(embed=embed)





@bot.command(aliases=['gangname'], pass_context=True)


async def gangnam(ctx):


    await bot.delete_message(ctx.message)


    images = ['https://media.giphy.com/media/nhtlzcG0ILnIQ/giphy.gif',


    'https://www.awesomegifs.com/wp-content/uploads/psy-gangnam-style-1.gif',


    'https://i.gifer.com/D0Qb.gif']


    embed = discord.Embed(color=0x0911ff)


    embed.set_image(url=random.choice(images))


    await bot.say(embed=embed)





@bot.command(pass_context=True)


async def idc(ctx):


    await bot.delete_message(ctx.message)


    images = ['https://media.giphy.com/media/TBQZjgYBihXtm/giphy.gif',


    'https://media0.giphy.com/media/DIZxVPeabWmBi/giphy.gif',


    'https://media1.tenor.com/images/f8be8d2a3e33b5074e5a3444cdd7ddd5/tenor.gif?itemid=4491535',


    'https://media0.giphy.com/media/MDd7k9STXFAEU/200.gif',


    'https://media.giphy.com/media/o3HEMUoTOEUWk/giphy.gif',


    'https://media.giphy.com/media/GSHoYf1kzkST6/giphy.gif',


    'https://media.giphy.com/media/18K2qcMKAgtPO/giphy.gif']


    embed = discord.Embed(color=0xff0027)


    embed.set_image(url=random.choice(images))


    await bot.say(embed=embed)





@bot.command(pass_context=True)


async def announce(ctx, *, xdd: str = None):


    if ctx.message.author.server_permissions.manage_server or ctx.message.author.id == OWNER_ID:


        await bot.delete_message(ctx.message)


        if xdd == None:


            await bot.say(f"{ctx.message.author.mention} ```Proper usage is\n\n>announce <Message to announce>```")


        else:


            await bot.send_message(ctx.message.author, f"Currently announcing to {len(ctx.message.server.members)} members\nThis might take some time")


            for member in ctx.message.server.members:


                try:


                    await bot.send_message(member, xdd)


                    print('Successfully sent a message to {}'.format(member.name))


                except:


                    pass


            await bot.send_message(ctx.message.author, "Successfully sent the announcment")


    else:


        embed = discord.Embed(title=noperm, color=0xff0000)


        await bot.say(embed=embed)








@bot.command(pass_context=True)


async def iplookup(ctx, *, site: str = None):


    if site == None:


        await bot.say(f"{ctx.message.author.mention} ```Proper usage is\n\n>iplookup <url>```")


    else:


        try:


            website = socket.gethostbyname(site)


            embed = discord.Embed(title="IP Lookup for website {}".format(site), description=website, color=0xbef482)


            await bot.say(embed=embed)


        except:


            await bot.say("That website does not exists")





#@bot.command(pass_context=True)


async def danken(ctx):


    chan = channel.name.upper().startswith





    channel_names = [


    'dank nigga', 'xddd', 'announcements plz', 'trump 2019', 'xDdDDd', 'hi im a channel',


    'gay lol', 'ur mom channel', 'area 51', 'ayy lmao', 'ruski channel', 'i drink vodka', 'rush b', 'rush a',


    'meme hub', 'kys here', 'dank wars', 'leet stuff lol', 'lmao', 'black people only', 'white people only', 'russians only',


    'americans are fat', 'drink bleach', 'gay people only', 'no niggas allowed', 'nsfw cuz of memes', 'no memes allowed wtf',


    'no normies', 'men only'


    ]





    nicknames = [


    'dank nigga', 'donald trump', 'roblox player xd', 'mincecraft player xd', 'mark zucc', 'owner of pornhub',


    'i am pro', 'nigga', 'true russian', 'cat', 'neko', 'dog', 'vodka', 'vodka drinker 24/7', 'autist',


    'white', 'Autism', 'watching porn', 'pr0 osu player', 'hardbass adidas', 'asian', 'racist nigga',


    '21 years old', 'blyat', 'cyka', 'psy', 'oppa gangnam style', 'ruski', 'russian me', 'im racist', 'im black',


    'im white', 'i eat water', 'melon juice', 'radio station'


    ]





    embed = discord.Embed(title=f"Renaming {len(ctx.message.server.channels)} channels", color=0x8035b8)


    await bot.say(embed=embed)





    for channel in ctx.message.server.channels:


        if chan('CHAT') or chan('GENERAL') or chan('MESSAGE'):


            await bot.edit_channel(channel, name="trump chat area")


        elif chan('BOT') or chan('COMMAND'):


            await bot.edit_channel(channel, name="do bot shit here")


        elif chan('SPAM'):


            await bot.edit_channel(channel, name="spam diz channel lmao")


        elif chan('ANNOUNCE'):


            await bot.edit_channel(channel, name="nigga dis is announcements")


        elif chan('NSFW'):


            await bot.edit_channel(channel, name=random.choice(['pornhub', 'send nudes here lol', 'nudes goes here']))


        elif chan('WELCOME') or chan('JOIN'):


            await bot.edit_channel(channel, name='whalecum channel')


        elif chan('IMPORTANT'):


            await bot.edit_channel(channel, name="important shit")


        elif chan('SELL'):


            await bot.edit_channel(channel, name='sell shit here lol')


        elif chan('BUY'):


            await bot.edit_channel(channel, name='buy shit here lol')


        elif chan('MARKET'):


            await bot.edit_channel(channel, name='dank market lmao')


        else:


            await bot.edit_channel(channel, name=random.choice(channel_names))


    embed = discord.Embed(title=f"Successfully finished renaming all {len(ctx.message.server.channels)} channels", color=0xff99b8)


    await bot.say(embed=embed)


    users = discord.Embed(title=f"Renaming {len(ctx.message.server.members)} members")


    await bot.say(embed=users)


    for member in ctx.message.server.members:


        try:


            await bot.change_nickname(member, random.choice(nicknames))


        except:


            await bot.send_message(ctx.message.author, f"Failed to rename {member.name}\nMake sure Coco BOT's role is higher than the highest role in {ctx.message.server.name}")





# Help


@bot.command(pass_context=True)


async def help(ctx):
    if ctx.message.author.bot:
      return
    else:
      author = ctx.message.author


    embed = discord.Embed(title="Coco BOT commands!, prefix is ( > )", description=">invite to invite", color=0xD1F1EA)

    embed.add_field(name="Moderator Commands", value="`kick`, `ban`, `slowpurge`, `warn`, `decide`, `secretban`, `secretkick`, `clear`, `slowmode`, `cslowmode`, `chaton`, `renamerole`, `renameserver`, `othernick`, `textchannel`, `voicechannel`, `allnicks`, `renamechannel`, `banall`, `kickall`,"


                         "`emojirename`, `purgechannels`, `announce`")





    embed.add_field(name="General Commands", value="`check`, `help`, `userinfo`, `botinfo`, `serverinfo`, `invite`, `membercount`, `servercount`, `websiteip`, "


                        "`avatar`, `say`, `embed`, `qr`, `google`, `youtube`, `imports`, `encode`, `vars`, `iplist`, `namelist`, `cardlist`, `randomint`, `ping`, `customint`, `embedcode`, `codeinfo`, `stringgen`, `realip`, `doxtools`, `report`, `botsearch`, `topbots`, `botdesc`, `serverowner`, `statcheck`, `gamecheck`, `vote`, `datacount`, `channelinfo`, `docs`, `nick`, `emojis`, `membernames`, `kickme`, `userip`, `gif`,  `iplookup`")





    embed.add_field(name="Fun Commands", value="**`meme`, `ask`, `kiss`, `hug`, `gender`, `fbi`, `joke`, `dadjoke`, `skincolor`, `dox`, `urmomgay`, "
        "`sapnupuas`, `gaycheck`, `hack`, `bomb`, `slap`, `game`, `whois`, `smashpass`, `rolldice`, `hairdye`, `dog`, `cat`, `height`, `talentcheck`, `howto`, `shoot`, `suicide`, `situation`, `lenny`, `autistcheck`, `changemymind`, `illegalize`, `angel`")



    embed.set_thumbnail(url=botavatar)


    await bot.send_message(author,embed=embed)
    await bot.say(DMs)






# On-Messages


@bot.event


async def on_message(message):





    if message.content.startswith(">"):


        print(f"{message.author.name} : {message.content}  (Server Name : {message.server.name} : {message.server.id}  {message.channel.id})")





    if message.content.startswith(">secretban"):


        await bot.delete_message(message)





    if message.content.startswith(">secretkick"):


        await bot.delete_message(message)





    if message.content.startswith(">say"):


        await bot.delete_message(message)




    if message.content.startswith(">warn"):


        await bot.delete_message(message)





    if message.content.startswith(">dm"):


        await bot.delete_message(message)





    if message.content == ">kick":


        await bot.send_message(message.channel, "{} ```Proper usage is\n\n>kick <mention a user>```".format(message.author.mention))





    if message.content == ">ioga|\| |>a|_|i_|a|<e |Da(_)|_ |_o9a|\| |Da(_)|_iig ioa iia ioi ioiyour mom gay":


        embed = discord.Embed(title="Congratulations for winning this game :D You got a cookie from me :cookie:", color=0xff0000)


        embed.set_image(url="https://media1.tenor.com/images/474cab58858485f27aebb351f4224d89/tenor.gif?itemid=4875606")


        await bot.send_message(message.author, embed=embed)





    if message.content == ">ban":


        await bot.send_message(message.channel, "{} ```Proper usage is\n\n>ban <mention a user>```".format(message.author.mention))





    if message.content == ">warn":


        await bot.send_message(message.channel, "{} ```Proper usage is\n>warn <mention a user>```".format(message.author.mention))





    if message.content == ">avatar":


        await bot.send_message(message.channel, "{} ```Proper usage is\n\n>avatar <mention a user>```".format(message.author.mention))





    if message.content == ">userinfo":


        await bot.send_message(message.channel, "{} ```Proper usage is\n\n>userinfo <mention a user>```".format(message.author.mention))





    if message.content == ">ask":


        await bot.send_message(message.channel, "{} ```Proper usage is\n\n>ask <question>```".format(message.author.mention))





    if message.content == ">say":


        await bot.send_message(message.channel, "{} ```Proper usage is\n\n>say <message>```".format(message.author.mention))





    if message.content == ">embed":


        await bot.send_message(message.channel, "{} ```Proper usage is\n\n>embed <message>```".format(message.author.mention))





    if message.content == ">qr":


        await bot.send_message(message.channel, "{} ```Proper usage is\n\n>qr <message>```".format(message.author.mention))





    if message.content == ">encode":


        await bot.send_message(message.channel, "{} ```Proper usage is\n\n>encode <message>```".format(message.author.mention))





    if message.content == ">google":


        await bot.send_message(message.channel, "{} ```Proper usage is\n\n>google <what do you wanna search on google>```".format(message.author.mention))





    if message.content == ">youtube":


        await bot.send_message(message.channel, "{} ```Proper usage is\n\n>youtube <what do you wanna search on youtube>```".format(message.author.mention))





    if message.content == ">kiss":


        await bot.send_message(message.channel, "{} ```Proper usage is\n\n>kiss <mention a user>```".format(message.author.mention))





    if message.content == ">hug":


        await bot.send_message(message.channel, "{} ```Proper usage is\n\n>hug <mention a user>```".format(message.author.mention))





    if message.content == ">gender":


        await bot.send_message(message.channel, "{} ```Proper usage is\n\n>gender <mention a user>```".format(message.author.mention))





    if message.content == ">virgin":


        await bot.send_message(message.channel, "{} ```Proper usage is\n\n>virgin <mention a user>```".format(message.author.mention))





    if message.content == ">skincolor":


        await bot.send_message(message.channel, "{} ```Proper usage is\n\n>skincolor <mention a user>```".format(message.author.mention))





    if message.content == ">clear'":


        await bot.send_message(message.channel, "{} ```Proper usage is\n\n>clear <pick amount of message 1-1000>```".format(message.author.mention))





    if message.content == ">startdox":


        await bot.send_message(message.channel, "{} ```Proper usage is\n\n>startdox <mention a user>```".format(message.author.mention))





    if message.content == ">dicksize":


        await bot.send_message(message.channel, "{} ```Proper usage is\n\n>dicksize <mention a user>```".format(message.author.mention))





    if message.content == ">customint":


        await bot.send_message(message.channel, "{} ```Proper usage is\n\n>customint <first number> <second number>```".format(message.author.mention))





    if message.content == ">gaycheck":


        await bot.send_message(message.channel, "{} ```Proper usage is\n\n>gaycheck <mention a user>```".format(message.author.mention))





    if message.content == ">hack":


        await bot.send_message(message.channel, "{} ```Proper usage is\n\n>hack <mention a user>```".format(message.author.mention))





    await bot.process_commands(message)

# Angel
@bot.command(pass_context=True)
async def angel(ctx):
    possible_responses = [
        "When you found your true love and your life will be happy again.", "There is a name Coco that can help you from anything.", "Find a knife and poke it to your self to commit suicide | its a fact but dont do it seriously.", "By the way you will find more friends", "You are gonna be successful if you do on where are you happy to do.", "Someone is spying you.", "You will see on your dream that you have a powers.", "Dont bully someone or it will gonna happen to you.", "Share your blessings if you want luckyness." ]
    await bot.say(random.choices(possible_responses))


@bot.command(pass_context=True)
async def poll(ctx, question, *options: str):
        if len(options) <= 1:
            await bot.say('You need more than one option to make a poll!')
            return
        if len(options) > 10:
            await bot.say('You cannot make a poll for more than 10 things!')
            return

        if len(options) == 2 and options[0] == 'yes' and options[1] == 'no':
            reactions = ['👍', '👎']
        else:
            reactions = [ '1\u20e3', '2\u20e3', '3\u20e3', '4\u20e3', '5\u20e3', '6\u20e3', '7\u20e3', '8\u20e3', '9\u20e3', '\U0001f51f']

        description = []
        for x, option in enumerate(options):
            description += '\n {} {}'.format(reactions[x], option)
            r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(title=question, description=''.join(description), color = discord.Color((r << 16) + (g << 8) + b))
        react_message = await bot.say(embed=embed)
        for reaction in reactions[:len(options)]:
            await bot.add_reaction(react_message, reaction)
        embed.set_footer(text='Poll ID: {}'.format(react_message.id))
        await bot.edit_message(react_message, embed=embed)




@bot.event
async def on_member_join(member):
    for channel in member.server.channels:
        if channel.name == '🎊welcome🎊':
            r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
            embed = discord.Embed(title=f'🎉Welcome {member.name} to {member.server.name}🎉', description='Please 🙏 do not forget to read the rules and dont try to break any one of them👼', color = discord.Color((r << 16) + (g << 8) + b))
            embed.add_field(name='__Thanks for joining__', value='**I hope you will be active here.😉**', inline=True)
            embed.set_thumbnail(url='https://media.giphy.com/media/OkJat1YNdoD3W/giphy.gif') 
            embed.set_image(url = member.avatar_url)
            embed.add_field(name='__Join position__', value='{}'.format(str(member.server.member_count)), inline=True)
            embed.add_field(name='Time of joining here', value=member.joined_at)
            await bot.send_message(channel, embed=embed) 

@bot.event
async def on_member_remove(member):
    for channel in member.server.channels:
        if channel.name == '🎊welcome🎊':
            r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
            embed = discord.Embed(title=f'{member.name} just left {member.server.name}', description='Good bye 👋! We will gonna miss you 😢', color = discord.Color((r << 16) + (g << 8) + b))
            embed.add_field(name='__User left__', value='**We hope you will be back soon 🙋.**', inline=True)
            embed.add_field(name='**Your join position was**', value=member.joined_at)
            embed.set_thumbnail(url=member.avatar_url)
            await bot.send_message(channel, embed=embed)


bot.run(os.getenv(Token))
