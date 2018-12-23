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

    user_add_xp(message.author.id, 2)
    if message.content.lower().startswith('mv!dailyrank'):
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        level=int(get_xp(message.author.id)/100)
        msgs=int(get_xp(message.author.id)/2)
        embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_author(name='Daily Universal Rank')
        embed.set_thumbnail(url = message.author.avatar_url)
        embed.add_field(name = '**__XP__**'.format(message.author),value ='``{}``'.format(get_xp(message.author.id)),inline = False)
        embed.add_field(name = '**__Level__**'.format(message.author),value ='``{}``'.format(level),inline = False)
        embed.add_field(name = '**__Messages__**'.format(message.author),value ='``{}`` Messages'.format(msgs),inline = False)
        embed.add_field(name='Note:',value='Our bot reset all ranks everyday so it shows only daily rank')
        await client.send_message(message.channel, embed=embed)
     
def user_add_xp(user_id: int, xp: int):
    if os.path.isfile("users.json"):
        try:
            with open('users.json', 'r') as fp:
                users = json.load(fp)
            users[user_id]['xp'] += xp
            with open('users.json', 'w') as fp:
                json.dump(users, fp, sort_keys=True, indent=4)
        except KeyError:
            with open('users.json', 'r') as fp:
                users = json.load(fp)
            users[user_id] = {}
            users[user_id]['xp'] = xp
            with open('users.json', 'w') as fp:
                json.dump(users, fp, sort_keys=True, indent=4)
    else:
        users = {user_id: {}}
        users[user_id]['xp'] = xp
        with open('users.json', 'w') as fp:
            json.dump(users, fp, sort_keys=True, indent=4)


def get_xp(user_id: int):
    if os.path.isfile('users.json'):
        with open('users.json', 'r') as fp:
            users = json.load(fp)
        return users[user_id]['xp']
    else:
        return 0
	               
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
