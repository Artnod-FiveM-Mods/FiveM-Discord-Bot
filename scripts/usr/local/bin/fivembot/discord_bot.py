#!/usr/bin/python3
#-*- coding: utf-8 -*-
'''
Created on 10 avr. 2018

@author: artnod
'''
import sys, asyncio, logging, logging.handlers
from subprocess import Popen, PIPE
from discord.ext import commands
from settings import BOT_CONF, LOG_CONF


# Set up a specific logger with our desired output level
my_logger = logging.getLogger('discord_bot')
my_logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fhandler = logging.handlers.RotatingFileHandler(
    '{}discord_bot.log'.format(LOG_CONF['log_dir']), 
    maxBytes = LOG_CONF['max_bytes'], 
    backupCount = LOG_CONF['backup_count']
)
fhandler.setLevel(logging.INFO)
# create console handler with a higher log level
chandler = logging.StreamHandler()
chandler.setLevel(logging.DEBUG)
# create formatter and add it to the handler
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
fhandler.setFormatter(formatter)
chandler.setFormatter(formatter)
# add the handler to logger
my_logger.addHandler(fhandler)
my_logger.addHandler(chandler)

bot = commands.Bot(command_prefix='/', description='A simple Bot to start/stop/update fivem server')

@bot.event
async def on_ready():
    """
    Bot Start
    """
    my_logger.debug(sys._getframe().f_code.co_name)
    print('Logged in as {} - {}'.format(bot.user.name, bot.user.id))

# start command
@bot.group(pass_context=True)
async def start(ctx):
    """
    \tStart a specific server
    
    Usage: /start <command>
    """
    my_logger.debug(sys._getframe().f_code.co_name)
    if ctx.invoked_subcommand is None:
        await bot.say('Failed !')
        await bot.say('Try **/help start** !')

@start.command(pass_context=True)
async def fivem(ctx):
    """
    \tStart fivem server
    
    Usage: /start fivem
    """
    my_logger.debug(sys._getframe().f_code.co_name)
    channel = ctx.message.channel
    member = ctx.message.author
    if channel.id == BOT_CONF['bot_channel']:
        if member.id in BOT_CONF['bot_admin_list']:
            await bot.say('**{0.name}** try to start ** fivem server**!\r'.format(member))
            try:
                my_logger.info('{0.name} try to start fivem server'.format(member))
                p = Popen(["service", "fivem", "start"], stdout=PIPE)
                toto = p.communicate()
                if toto[0] != None:
                    await bot.say(toto[0].decode('unicode_escape'))
                else:
                    await bot.say(toto[1].decode('unicode_escape'))
            except:
                my_logger.err('Command Failed')
                await bot.say('Command Failed!')
        else:
            my_logger.warn('{0.name} Access Denied'.format(member))
            await bot.say('**{0.name}** ! Access Denied!\r'.format(member))
    else:
        my_logger.warn('{0.name} Bad channel'.format(member))
        await bot.say('**{0.name}** ! Bad channel!\r'.format(member))


# stop command
@bot.group(pass_context=True)
async def stop(ctx):
    """
    \tStop a specific server
    
    Usage: /stop <command>
    """
    my_logger.debug(sys._getframe().f_code.co_name)
    if ctx.invoked_subcommand is None:
        await bot.say('Failed !')
        await bot.say('Try **/help stop** !')

@stop.command(pass_context=True)
async def fivem(ctx):
    """
    \tStop fivem server
    
    Usage: /stop fivem
    """
    my_logger.debug(sys._getframe().f_code.co_name)
    channel = ctx.message.channel
    member = ctx.message.author
    if channel.id == BOT_CONF['bot_channel']:
        if member.id in BOT_CONF['bot_admin_list']:
            await bot.say('**{0.name}** try to stop ** fivem server**!\r'.format(member))
            try:
                my_logger.info('{0.name} try to stop fivem server'.format(member))
                p = Popen(["service", "fivem", "stop"], stdout=PIPE)
                toto = p.communicate()
                if toto[0] != None:
                    await bot.say(toto[0].decode('unicode_escape'))
                else:
                    await bot.say(toto[1].decode('unicode_escape'))
            except:
                my_logger.err('Command Failed')
                await bot.say('Command Failed!')
        else:
            my_logger.warn('{0.name} Access Denied'.format(member))
            await bot.say('**{0.name}** ! Access Denied!\r'.format(member))
            
    else:
        my_logger.warn('{0.name} Bad channel'.format(member))
        await bot.say('**{0.name}** ! Bad channel!\r'.format(member))


# update command
@bot.group(pass_context=True)
async def update(ctx):
    """
    \tUpdate a specific resource
    
    Usage: /update <command>
    """
    my_logger.debug(sys._getframe().f_code.co_name)
    if ctx.invoked_subcommand is None:
        await bot.say('Failed !')
        await bot.say('Try **/help update** !')

@update.command(pass_context=True)
async def esx_races(ctx):
    """
    \tUpdate esx_races
    
    Usage: /update esx_races
    """
    my_logger.debug(sys._getframe().f_code.co_name)
    channel = ctx.message.channel
    member = ctx.message.author
    if channel.id == BOT_CONF['bot_channel']:
        if member.id in BOT_CONF['bot_admin_list']:
            await bot.say('**{0.name}** try to update **esx_races**!\r'.format(member))
            try:
                my_logger.info('{0.name} try to update esx_races'.format(member))
                p = Popen(["/root/fmm/update.sh", "-r"], stdout=PIPE)
                toto = p.communicate()
                if toto[0] != None:
                    await bot.say(toto[0].decode('unicode_escape'))
                else:
                    await bot.say(toto[1].decode('unicode_escape'))
            except:
                my_logger.err('Command Failed')
                await bot.say('Command Failed!')
        else:
            my_logger.warn('{0.name} Access Denied'.format(member))
            await bot.say('**{0.name}** ! Access Denied!\r'.format(member))
            
    else:
        my_logger.warn('{0.name} Bad channel'.format(member))
        await bot.say('**{0.name}** ! Bad channel!\r'.format(member))

@update.command(pass_context=True)
async def esx_brinks(ctx):
    """
    \tUpdate esx_brinks
    
    Usage: /update esx_brinks
    """
    my_logger.debug(sys._getframe().f_code.co_name)
    channel = ctx.message.channel
    member = ctx.message.author
    if channel.id == BOT_CONF['bot_channel']:
        if member.id in BOT_CONF['bot_admin_list']:
            await bot.say('**{0.name}** try to update **esx_brinks**!\r'.format(member))
            try:
                my_logger.info('{0.name} try to update esx_brinks'.format(member))
                p = Popen(["/root/fmm/update.sh", "-b"], stdout=PIPE)
                toto = p.communicate()
                if toto[0] != None:
                    await bot.say(toto[0].decode('unicode_escape'))
                else:
                    await bot.say(toto[1].decode('unicode_escape'))
            except:
                my_logger.err('Command Failed')
                await bot.say('Command Failed!')
        else:
            my_logger.warn('{0.name} Access Denied'.format(member))
            await bot.say('**{0.name}** ! Access Denied!\r'.format(member))
            
    else:
        my_logger.warn('{0.name} Bad channel'.format(member))
        await bot.say('**{0.name}** ! Bad channel!\r'.format(member))

@update.command(pass_context=True)
async def esx_journalist(ctx):
    """
    \tUpdate esx_journalist
    
    Usage: /update esx_journalist
    """
    my_logger.debug(sys._getframe().f_code.co_name)
    channel = ctx.message.channel
    member = ctx.message.author
    if channel.id == BOT_CONF['bot_channel']:
        if member.id in BOT_CONF['bot_admin_list']:
            await bot.say('**{0.name}** try to update **esx_journalist**!\r'.format(member))
            try:
                my_logger.info('{0.name} try to update esx_journalist'.format(member))
                p = Popen(["/root/fmm/update.sh", "-j"], stdout=PIPE)
                toto = p.communicate()
                if toto[0] != None:
                    await bot.say(toto[0].decode('unicode_escape'))
                else:
                    await bot.say(toto[1].decode('unicode_escape'))
            except:
                my_logger.err('Command Failed')
                await bot.say('Command Failed!')
        else:
            my_logger.warn('{0.name} Access Denied'.format(member))
            await bot.say('**{0.name}** ! Access Denied!\r'.format(member))
            
    else:
        my_logger.warn('{0.name} Bad channel'.format(member))
        await bot.say('**{0.name}** ! Bad channel!\r'.format(member))

# main
if __name__ == '__main__':
    my_logger.info('Start Discord Bot')
    bot.run(BOT_CONF['bot_token'])
    
