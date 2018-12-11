import discord
import asyncio
from discord.ext.commands import Bot
import platform
import time
import os
import colorsys
import random
import json
from os import environ
 
bot = Bot(description="Coco BOT is best", command_prefix=">", pm_help = False)
bot.remove_command('help')

@bot.event
async def on_ready():
    print('Logged in as '+bot.user.name+' (ID:'+bot.user.id+') | Connected to '+str(len(bot.servers))+' servers | Connected to '+str(len(set(bot.get_all_members())))+' users')
    print('--------')
    print('--------')
    print('Started Coco BOT')
    print('Created by Coco')
 
 
@bot.event
async def on_message_edit(before, after):
    if before.content == after.content:
      return
    if before.author == bot.user:
      return
    else:
      user = before.author
      member = after.author
      for channel in user.server.channels:
        if channel.name == 'coco-bot-logs':
            r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
            embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
            embed.set_author(name='Message edited')
            embed.add_field(name = 'User: **{0}**'.format(user.name),value ='UserID: **{}**'.format(user.id),inline = False)
            embed.add_field(name = 'Before:',value ='{}'.format(before.content),inline = False)
            embed.add_field(name = 'After:',value ='{}'.format(after.content),inline = False)
            embed.add_field(name = 'Channel:',value ='{}'.format(before.channel.name),inline = False)
            await bot.send_message(channel, embed=embed)
 
@bot.event
async def on_message_delete(message):
    if not message.author.bot:
      channelname = 'coco-bot-logs'
      logchannel=None
      for channel in message.server.channels:
        if channel.name == channelname:
          user = message.author
      for channel in user.server.channels:
        if channel.name == 'coco-bot-logs':
          logchannel = channel
          r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
          embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
          embed.set_author(name='Message deleted')
          embed.add_field(name = 'User: **{0}**'.format(user.name),value ='UserID: **{}**'.format(user.id),inline = False)
          embed.add_field(name = 'Message:',value ='{}'.format(message.content),inline = False)
          embed.add_field(name = 'Channel:',value ='{}'.format(message.channel.name),inline = False)
          await bot.send_message(logchannel,  embed=embed)
          
          
@bot.event
async def on_reaction_add(reaction, user):
  for channel in user.server.channels:
    if channel.name == 'coco-bot-logs':
        logchannel = channel
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_author(name='Reaction Added')
        embed.add_field(name = 'User: **{0}**'.format(user.name),value ='UserID: **{}**'.format(user.id),inline = False)
        embed.add_field(name = 'Message:',value ='{}'.format(reaction.message.content),inline = False)
        embed.add_field(name = 'Channel:',value ='{}'.format(reaction.message.channel.name),inline = False)
        embed.add_field(name = 'Emoji:',value ='{}'.format(reaction.emoji),inline = False)
        await bot.send_message(logchannel,  embed=embed)
        
@bot.event
async def on_reaction_remove(reaction, user):
  for channel in user.server.channels:
    if channel.name == 'coco-bot-logs':
        logchannel = channel
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_author(name='Reaction Removed')
        embed.add_field(name = 'User: **{0}**'.format(user.name),value ='UserID: **{}**'.format(user.id),inline = False)
        embed.add_field(name = 'Message:',value ='{}'.format(reaction.message.content),inline = False)
        embed.add_field(name = 'Channel:',value ='{}'.format(reaction.message.channel.name),inline = False)
        embed.add_field(name = 'Emoji:',value ='{}'.format(reaction.emoji),inline = False)
        await bot.send_message(logchannel,  embed=embed)
 
 
@bot.event
async def on_message(message):
    user = message.author
    if message.author.bot:
      return
    if message.content.startswith('>say'):
      return
    else:
      if message.content.startswith('>donate'):
          msg = '**Support us by donating us;** https://www.paypal.me/CocoGT'
          await bot.send_message(message.channel, msg)
          
      if 'Who is your creator <@!24791747004989441>?' in message.content:
          msg = 'Coco#6429 is my creator'.format(message)
          msg2 = await bot.send_message(message.channel, msg)
         
      if 'hi <@!24791747004989441>' in message.content:
          msg = 'Hello {}'.format(message.author.name)
          msg2 = await bot.send_message(message.channel, msg)
         
      if 'bye <@!24791747004989441>' in message.content:
          msg = 'Bye {}'.format(message.author.name)
          msg2 = await bot.send_message(message.channel, msg)
         
      if 'Bye <@!24791747004989441>' in message.content:
          msg = 'Bye {}'.format(message.author.name)
          msg2 = await bot.send_message(message.channel, msg)
                 
      if 'hello <@!24791747004989441>' in message.content:
          msg = 'Hello {}'.format(message.author.name)
          msg2 = await bot.send_message(message.channel, msg)
         
      if 'Hi <@!24791747004989441>' in message.content:
          msg = 'Hello {}'.format(message.author.name)
          msg2 = await bot.send_message(message.channel, msg)
          
      if 'Hello <@!24791747004989441>' in message.content:
          msg = 'Hello {}'.format(message.author.name)
          msg2 = await bot.send_message(message.channel, msg)
          
      if 'how are you <@!24791747004989441>?' in message.content:
          msg = 'I am fine what about you? {}'.format(message.author.name)
          msg2 = await bot.send_message(message.channel, msg)
         
      if 'How are you <@!24791747004989441>?' in message.content:
          msg = 'I am fine what about you? {}'.format(message.author.name)
          msg2 = await bot.send_message(message.channel, msg)
          
      if 'sup <@!24791747004989441>' in message.content:
          msg = 'I am fine what about you? {}'.format(message.author.name)
          msg2 = await bot.send_message(message.channel, msg)
         
      if 'Sup <@!24791747004989441>' in message.content:
          msg = 'I am fine what about you? {}'.format(message.author.name)
          msg2 = await bot.send_message(message.channel, msg)         
          
      if 'I am also fine <@!24791747004989441>' in message.content:
          msg = 'Cool! {}'.format(message.author.name)
          msg2 = await bot.send_message(message.channel, msg)          
         
      if 'i am also fine <@!24791747004989441>' in message.content:
          msg = 'Cool! {}'.format(message.author.name)
          msg2 = await bot.send_message(message.channel, msg)          
          
      if 'fuck' in message.content:
          msg = 'Do not use bad words {0.author.name}'.format(message)
          msg2 = await bot.send_message(message.channel, msg)
          await bot.delete_message(message)
          await asyncio.sleep(5)
          await bot.delete_message(msg2)
          for channel in user.server.channels:
            if channel.name == 'coco-bot-logs':
                r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
                embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
                embed.set_author(name='Warned user')
                embed.add_field(name = 'User: **{0}**'.format(user.name),value ='UserID: **{}**'.format(user.id),inline = False)
                embed.add_field(name = 'Reason: **Used bad words**',value ='Word: **fuck**',inline = False)
                embed.add_field(name = 'Type of bad word:',value ='English bad word',inline = False)
                embed.add_field(name = 'Channel:',value ='{}'.format(message.channel.name),inline = False)
                embed.add_field(name = 'Message:',value ='{}'.format(message.content),inline = False)
                await bot.send_message(channel, embed=embed)
      
      if 'FUCK' in message.content:
          msg = 'Do not use bad words {0.author.name}'.format(message)
          msg2 = await bot.send_message(message.channel, msg)
          await bot.delete_message(message)
          await asyncio.sleep(5)
          await bot.delete_message(msg2)
          for channel in user.server.channels:
            if channel.name == 'coco-bot-logs':
                r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
                embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
                embed.set_author(name='Warned user')
                embed.add_field(name = 'User: **{0}**'.format(user.name),value ='UserID: **{}**'.format(user.id),inline = False)
                embed.add_field(name = 'Reason: **Used bad words**',value ='Word: **FUCK**',inline = False)
                embed.add_field(name = 'Type of bad word:',value ='English bad word',inline = False)
                embed.add_field(name = 'Channel:',value ='{}'.format(message.channel.name),inline = False)
                embed.add_field(name = 'Message:',value ='{}'.format(message.content),inline = False)
                await bot.send_message(channel, embed=embed)
        
      if 'asshole' in message.content:
          msg = 'Do not use bad words {0.author.name}'.format(message)
          msg2 = await bot.send_message(message.channel, msg)
          await bot.delete_message(message)
          await asyncio.sleep(5)
          await bot.delete_message(msg2)
          for channel in user.server.channels:
            if channel.name == 'coco-bot-logs':
                r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
                embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
                embed.set_author(name='Warned user')
                embed.add_field(name = 'User: **{0}**'.format(user.name),value ='UserID: **{}**'.format(user.id),inline = False)
                embed.add_field(name = 'Reason: **Used bad words**',value ='Word: **asshole**',inline = False)
                embed.add_field(name = 'Type of bad word:',value ='English bad word',inline = False)
                embed.add_field(name = 'Channel:',value ='{}'.format(message.channel.name),inline = False)
                embed.add_field(name = 'Message:',value ='{}'.format(message.content),inline = False)
                await bot.send_message(channel, embed=embed)
        
      if 'ASSHOLE' in message.content:
          msg = 'Do not use bad words {0.author.name}'.format(message)
          msg2 = await bot.send_message(message.channel, msg)
          await bot.delete_message(message)
          await asyncio.sleep(5)
          await bot.delete_message(msg2)
          for channel in user.server.channels:
            if channel.name == 'coco-bot-logs':
                r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
                embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
                embed.set_author(name='Warned user')
                embed.add_field(name = 'User: **{0}**'.format(user.name),value ='UserID: **{}**'.format(user.id),inline = False)
                embed.add_field(name = 'Reason: **Used bad words**',value ='Word: **ASSHOLE**',inline = False)
                embed.add_field(name = 'Type of bad word:',value ='English bad word',inline = False)
                embed.add_field(name = 'Channel:',value ='{}'.format(message.channel.name),inline = False)
                embed.add_field(name = 'Message:',value ='{}'.format(message.content),inline = False)
                await bot.send_message(channel, embed=embed)
                
      if 'Fuck' in message.content:
          msg = 'Do not use bad words {0.author.name}'.format(message)
          msg2 = await bot.send_message(message.channel, msg)
          await bot.delete_message(message)
          await asyncio.sleep(5)
          await bot.delete_message(msg2)
          for channel in user.server.channels:
            if channel.name == 'coco-bot-logs':
                r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
                embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
                embed.set_author(name='Warned user')
                embed.add_field(name = 'User: **{0}**'.format(user.name),value ='UserID: **{}**'.format(user.id),inline = False)
                embed.add_field(name = 'Reason: **Used bad words**',value ='Word: **Fuck**',inline = False)
                embed.add_field(name = 'Type of bad word:',value ='English bad word',inline = False)
                embed.add_field(name = 'Channel:',value ='{}'.format(message.channel.name),inline = False)
                embed.add_field(name = 'Message:',value ='{}'.format(message.content),inline = False)
                await bot.send_message(channel, embed=embed)
        
      if 'porn' in message.content:
          msg = 'Do not use bad words {0.author.name}'.format(message)
          msg2 = await bot.send_message(message.channel, msg)
          await bot.delete_message(message)
          await asyncio.sleep(5)
          await bot.delete_message(msg2)
          for channel in user.server.channels:
            if channel.name == 'coco-bot-logs':
                r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
                embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
                embed.set_author(name='Warned user')
                embed.add_field(name = 'User: **{0}**'.format(user.name),value ='UserID: **{}**'.format(user.id),inline = False)
                embed.add_field(name = 'Reason: **Used bad words**',value ='Word: **porn**',inline = False)
                embed.add_field(name = 'Type of bad word:',value ='English bad word',inline = False)
                embed.add_field(name = 'Message:',value ='{}'.format(message.content),inline = False)
                embed.add_field(name = 'Channel:',value ='{}'.format(message.channel.name),inline = False)
                await bot.send_message(channel, embed=embed)
        
      if 'idiot' in message.content:
          msg = 'Do not use bad words {0.author.name}'.format(message)
          msg2 = await bot.send_message(message.channel, msg)
          await bot.delete_message(message)
          await asyncio.sleep(5)
          await bot.delete_message(msg2)
          for channel in user.server.channels:
            if channel.name == 'coco-bot-logs':
                r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
                embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
                embed.set_author(name='Warned user')
                embed.add_field(name = 'User: **{0}**'.format(user.name),value ='UserID: **{}**'.format(user.id),inline = False)
                embed.add_field(name = 'Reason: **Used bad words**',value ='Word: **idiot**',inline = False)
                embed.add_field(name = 'Type of bad word:',value ='English bad word',inline = False)
                embed.add_field(name = 'Channel:',value ='{}'.format(message.channel.name),inline = False)
                embed.add_field(name = 'Message:',value ='{}'.format(message.content),inline = False)
                await bot.send_message(channel, embed=embed)
        
      if 'Porn' in message.content:
          msg = 'Do not use bad words {0.author.name}'.format(message)
          msg2 = await bot.send_message(message.channel, msg)
          await bot.delete_message(message)
          await asyncio.sleep(5)
          await bot.delete_message(msg2)
          for channel in user.server.channels:
            if channel.name == 'coco-bot-logs':
                r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
                embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
                embed.set_author(name='Warned user')
                embed.add_field(name = 'User: **{0}**'.format(user.name),value ='UserID: **{}**'.format(user.id),inline = False)
                embed.add_field(name = 'Reason: **Used bad words**',value ='Word: **Porn**',inline = False)
                embed.add_field(name = 'Type of bad word:',value ='English bad word',inline = False)
                embed.add_field(name = 'Channel:',value ='{}'.format(message.channel.name),inline = False)
                embed.add_field(name = 'Message:',value ='{}'.format(message.content),inline = False)
                await bot.send_message(channel, embed=embed)
       
      if 'bitch' in message.content:
          msg = 'Do not use bad words {0.author.name}'.format(message)
          msg2 = await bot.send_message(message.channel, msg)
          await bot.delete_message(message)
          await asyncio.sleep(5)
          await bot.delete_message(msg2)
          for channel in user.server.channels:
            if channel.name == 'coco-bot-logs':
                r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
                embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
                embed.set_author(name='Warned user')
                embed.add_field(name = 'User: **{0}**'.format(user.name),value ='UserID: **{}**'.format(user.id),inline = False)
                embed.add_field(name = 'Reason: **Used bad words**',value ='Word: **bitch**',inline = False)
                embed.add_field(name = 'Type of bad word:',value ='English bad word(Shortform abuse)',inline = False)
                embed.add_field(name = 'Channel:',value ='{}'.format(message.channel.name),inline = False)
                embed.add_field(name = 'Message:',value ='{}'.format(message.content),inline = False)
                await bot.send_message(channel, embed=embed)

      if 'Bitch' in message.content:
          msg = 'Do not use bad words {0.author.name}'.format(message)
          msg2 = await bot.send_message(message.channel, msg)
          await bot.delete_message(message)
          await asyncio.sleep(5)
          await bot.delete_message(msg2)
          for channel in user.server.channels:
            if channel.name == 'coco-bot-logs':
                r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
                embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
                embed.set_author(name='Warned user')
                embed.add_field(name = 'User: **{0}**'.format(user.name),value ='UserID: **{}**'.format(user.id),inline = False)
                embed.add_field(name = 'Reason: **Used bad words**',value ='Word: **Bitch**',inline = False)
                embed.add_field(name = 'Type of bad word:',value ='English bad word(Shortform abuse)',inline = False)
                embed.add_field(name = 'Channel:',value ='{}'.format(message.channel.name),inline = False)
                embed.add_field(name = 'Message:',value ='{}'.format(message.content),inline = False)
                await bot.send_message(channel, embed=embed)

      if 'pussy' in message.content:
          msg = 'Do not use bad words {0.author.name}'.format(message)
          msg2 = await bot.send_message(message.channel, msg)
          await bot.delete_message(message)
          await asyncio.sleep(5)
          await bot.delete_message(msg2)
          for channel in user.server.channels:
            if channel.name == 'coco-bot-logs':
                r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
                embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
                embed.set_author(name='Warned user')
                embed.add_field(name = 'User: **{0}**'.format(user.name),value ='UserID: **{}**'.format(user.id),inline = False)
                embed.add_field(name = 'Reason: **Used bad words**',value ='Word: **pussy**',inline = False)
                embed.add_field(name = 'Type of bad word:',value ='English bad word(Short form abuse)',inline = False)
                embed.add_field(name = 'Channel:',value ='{}'.format(message.channel.name),inline = False)
                embed.add_field(name = 'Message:',value ='{}'.format(message.content),inline = False)
                await bot.send_message(channel, embed=embed)

      if 'Shit' in message.content:
          msg = 'Do not use bad words {0.author.name}'.format(message)
          msg2 = await bot.send_message(message.channel, msg)
          await bot.delete_message(message)
          await asyncio.sleep(5)
          await bot.delete_message(msg2)
          for channel in user.server.channels:
            if channel.name == 'coco-bot-logs':
                r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
                embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
                embed.set_author(name='Warned user')
                embed.add_field(name = 'User: **{0}**'.format(user.name),value ='UserID: **{}**'.format(user.id),inline = False)
                embed.add_field(name = 'Reason: **Used bad words**',value ='Word: **Shit**',inline = False)
                embed.add_field(name = 'Type of bad word:',value ='English bad word(Short form abuse)',inline = False)
                embed.add_field(name = 'Channel:',value ='{}'.format(message.channel.name),inline = False)
                embed.add_field(name = 'Message:',value ='{}'.format(message.content),inline = False)
                await bot.send_message(channel, embed=embed)

      if 'shit' in message.content:
          msg = 'Do not use bad words {0.author.name}'.format(message)
          msg2 = await bot.send_message(message.channel, msg)
          await bot.delete_message(message)
          await asyncio.sleep(5)
          await bot.delete_message(msg2)
          for channel in user.server.channels:
            if channel.name == 'coco-bot-logs':
                r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
                embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
                embed.set_author(name='Warned user')
                embed.add_field(name = 'User: **{0}**'.format(user.name),value ='UserID: **{}**'.format(user.id),inline = False)
                embed.add_field(name = 'Reason: **Used bad words**',value ='Word: **shit**',inline = False)
                embed.add_field(name = 'Type of bad word:',value ='English bad word(Short form abuse)',inline = False)
                embed.add_field(name = 'Channel:',value ='{}'.format(message.channel.name),inline = False)
                embed.add_field(name = 'Message:',value ='{}'.format(message.content),inline = False)
                await bot.send_message(channel, embed=embed)

      if 'Pussy' in message.content:
          msg = 'Do not use bad words {0.author.name}'.format(message)
          msg2 = await bot.send_message(message.channel, msg)
          await bot.delete_message(message)
          await asyncio.sleep(5)
          await bot.delete_message(msg2)
          for channel in user.server.channels:
            if channel.name == 'coco-bot-logs':
                r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
                embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
                embed.set_author(name='Warned user')
                embed.add_field(name = 'User: **{0}**'.format(user.name),value ='UserID: **{}**'.format(user.id),inline = False)
                embed.add_field(name = 'Reason: **Used bad words**',value ='Word: **Pussy**',inline = False)
                embed.add_field(name = 'Type of bad word:',value ='English bad word(Short form abuse)',inline = False)
                embed.add_field(name = 'Channel:',value ='{}'.format(message.channel.name),inline = False)
                embed.add_field(name = 'Message:',value ='{}'.format(message.content),inline = False)
                await bot.send_message(channel, embed=embed)

      if 'Dick' in message.content:
          msg = 'Do not use bad words {0.author.name}'.format(message)
          msg2 = await bot.send_message(message.channel, msg)
          await bot.delete_message(message)
          await asyncio.sleep(5)
          await bot.delete_message(msg2)
          for channel in user.server.channels:
            if channel.name == 'coco-bot-logs':
                r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
                embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
                embed.set_author(name='Warned user')
                embed.add_field(name = 'User: **{0}**'.format(user.name),value ='UserID: **{}**'.format(user.id),inline = False)
                embed.add_field(name = 'Reason: **Used bad words**',value ='Word: **Dick**',inline = False)

      if 'dick ' in message.content:
          msg = 'Do not use bad words {0.author.name}'.format(message)
          msg2 = await bot.send_message(message.channel, msg)
          await bot.delete_message(message)
          await asyncio.sleep(5)
          await bot.delete_message(msg2)
          for channel in user.server.channels:
            if channel.name == 'coco-bot-logs':
                r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
                embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
                embed.set_author(name='Warned user')
                embed.add_field(name = 'User: **{0}**'.format(user.name),value ='UserID: **{}**'.format(user.id),inline = False)
                embed.add_field(name = 'Reason: **Used bad words**',value ='Word: **dick**',inline = False)
                embed.add_field(name = 'Type of bad word:',value ='English bad word(Short form abuse)',inline = False)
                embed.add_field(name = 'Channel:',value ='{}'.format(message.channel.name),inline = False)
                embed.add_field(name = 'Message:',value ='{}'.format(message.content),inline = False)
                await bot.send_message(channel, embed=embed)

      if 'dick' in message.content:
          msg = 'Do not use bad words {0.author.name}'.format(message)
          msg2 = await bot.send_message(message.channel, msg)
          await bot.delete_message(message)
          await asyncio.sleep(5)
          await bot.delete_message(msg2)
          for channel in user.server.channels:
            if channel.name == 'coco-bot-logs':
                r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
                embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
                embed.set_author(name='Warned user')
                embed.add_field(name = 'User: **{0}**'.format(user.name),value ='UserID: **{}**'.format(user.id),inline = False)
                embed.add_field(name = 'Reason: **Used bad words**',value ='Word: **dick**',inline = False)
                embed.add_field(name = 'Type of bad word:',value ='English bad word(Short form abuse)',inline = False)
                embed.add_field(name = 'Channel:',value ='{}'.format(message.channel.name),inline = False)
                embed.add_field(name = 'Message:',value ='{}'.format(message.content),inline = False)
                await bot.send_message(channel, embed=embed)

@bot.event
async def on_member_join(member):
    for channel in member.server.channels:
        if channel.name == 'welcome':
            r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
            embed = discord.Embed(title=f'Welcome {member.name} to {member.server.name}', description='Please  do not forget to read the rules and dont try to break any one of them', color = discord.Color((r << 16) + (g << 8) + b))
            embed.add_field(name='__Thanks for joining__', value='**I hope you will be active here.**', inline=True)
            embed.set_thumbnail(url='https://media.giphy.com/media/OkJat1YNdoD3W/giphy.gif') 
            embed.set_image(url = member.avatar_url)
            embed.add_field(name='__Join position__', value='{}'.format(str(member.server.member_count)), inline=True)
            embed.add_field(name='Time of joining here', value=member.joined_at)
            await bot.send_message(channel, embed=embed) 

@bot.event
async def on_member_remove(member):
    for channel in member.server.channels:
        if channel.name == 'welcome':
            r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
            embed = discord.Embed(title=f'{member.name} just left {member.server.name}', description='Good bye ! We will gonna miss you ', color = discord.Color((r << 16) + (g << 8) + b))
            embed.add_field(name='__User left__', value='**We hope you will be back soon .**', inline=True)
            embed.add_field(name='**Your join position was**', value=member.joined_at)
            embed.set_thumbnail(url=member.avatar_url)
            await bot.send_message(channel, embed=embed)

@bot.event
async def on_member_join(member):
    for channel in member.server.channels:
        if channel.name == '★彡-welcome-彡★':
            r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
            embed = discord.Embed(title=f'Welcome {member.name} to {member.server.name}', description='Please  do not forget to read the rules and dont try to break any one of them', color = discord.Color((r << 16) + (g << 8) + b))
            embed.add_field(name='__Thanks for joining__', value='**I hope you will be active here.**', inline=True)
            embed.set_thumbnail(url='https://media.giphy.com/media/OkJat1YNdoD3W/giphy.gif') 
            embed.set_image(url = member.avatar_url)
            embed.add_field(name='__Join position__', value='{}'.format(str(member.server.member_count)), inline=True)
            embed.add_field(name='Time of joining here', value=member.joined_at)
            await bot.send_message(channel, embed=embed) 

@bot.event
async def on_member_remove(member):
    for channel in member.server.channels:
        if channel.name == '★彡-welcome-彡★':
            r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
            embed = discord.Embed(title=f'{member.name} just left {member.server.name}', description='Good bye! We will gonna miss you ', color = discord.Color((r << 16) + (g << 8) + b))
            embed.add_field(name='__User left the server__', value='**We hope you will be back soon.**', inline=True)
            embed.add_field(name='**👇Your join position here was👇**', value=member.joined_at)
            embed.set_thumbnail(url=member.avatar_url)
            await bot.send_message(channel, embed=embed)



bot.run(os.environ['Token'])
