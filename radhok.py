import discord
from discord.ext import commands
import os
import random
import json
import asyncio
import time

client = commands.Bot(description="Blackfox Official Bot", command_prefix=commands.when_mentioned_or("^"), pm_help = True)
client.remove_command('help')

@client.event
async def on_message(message):
    with open("users.json", "r") as f:
        users = json.load(f)
        if message.author.bot:
            return
        if message.channel.is_private:
            return
        else:
            await update_data(users, message.author, message.server)
            number = random.randint(5,10)
            await add_experience(users, message.author, number, message.server)
            await level_up(users, message.author, message.channel, message.server)

        with open("users.json", "w") as f:
            json.dump(users, f)
    await client.process_commands(message)

async def update_data(users, user, server):
    if not user.id + "-" + server.id in users:
        users[user.id + "-" + server.id] = {}
        users[user.id + "-" + server.id]["experience"] = 0
        users[user.id + "-" + server.id]["level"] = 1
        users[user.id + "-" + server.id]["last_message"] = 0

async def add_experience(users, user, exp, server):
    if time.time() - users[user.id + "-" + server.id]["last_message"] > 5: 
        users[user.id + "-" + server.id]["experience"] += exp
        users[user.id + "-" + server.id]["last_message"] = time.time()
    else:
        return

async def level_up(users, user, channel, server):
    experience = users[user.id + "-" + server.id]["experience"]
    lvl_start = users[user.id + "-" + server.id]["level"]
    lvl_end = int(experience ** (1/4))
    if lvl_start < lvl_end:
        await client.send_message(channel, f":tada: Congrats {user.name}, you levelled up to level {lvl_end}!")
        users[user.id + "-" + server.id]["level"] = lvl_end

#show when it connects to discord
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)

@client.event
async def on_reaction_add(reaction, user):
    roleChannelId = discord.utils.get(reaction.message.server.channels, name="★verify-for-chatting★", type="ChannelType.voice") 

    if reaction.message.channel != roleChannelId:
        return #So it only happens in the specified channel
    if str(reaction.emoji) == "🇻":
        role = discord.utils.get(reaction.message.server.roles, name="Verified")
        await client.add_roles(user, role)

@client.event
async def on_reaction_remove(reaction, user):
    verifychannel = "★verify-for-chatting★"
    for channel in user.server.channels:
      if channel.name != verifychannel:
          return
      if str(reaction.emoji) == "🇻":
          role = discord.utils.get(user.server.roles, name="Verified")
          await client.remove_roles(user, role)

@client.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def setreactionverify(ctx):
    author = ctx.message.author
    server = ctx.message.server
    everyone_perms = discord.PermissionOverwrite(send_messages=False,read_messages=True)
    everyone = discord.ChannelPermissions(target=server.default_role, overwrite=everyone_perms)
    await client.create_channel(server, '★verify-for-chatting★',everyone)
    for channel in author.server.channels:
        if channel.name == '★verify-for-chatting★':
            react_message = await client.send_message(channel, 'React with 🇻 to Verify | Sometimes it not works so you can also use mv!verify anywhere(Where you can send messages)')
            reaction = '🇻'
            await client.add_reaction(react_message, reaction)


client.run(os.getenv('Token'))
