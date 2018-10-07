#!/usr/bin/python3
#-*- coding: utf-8 -*-
'''
Created on 12 avr. 2018

@author: artnod
'''

BOT_CONF = {
    'bot_token' : '<token>',
    'bot_channel' : '<channel>',
    'bot_admin_list' : ('<user>',),
}

WEBHOOK_CONF = {
    'webhook_url' : '<webhook_url>',
    'message' : {
        'author' : 'Toto Le Robot',
        'author_icon' : 'https://discordapp.com/assets/6debd47ed13483642cf09e832ed0bc1b.png',
        'thumbnail_on' : 'https://i.pinimg.com/originals/23/4a/6b/234a6b9a897c7e963bf73ef073b94842.jpg',
        'thumbnail_off' : 'http://www.clker.com/cliparts/4/4/1/a/1195429270821624493molumen_multicolor_power_buttons_4.svg.hi.png',
        'footer' : 'http://www.4forcesclan.com/images/7dlogo.png',
    }
}

FIVEM_CONF = {
    'server_name' : '<serverName>',
    'server_ip'   : '<IP>',
    'server_port' : 30120,
}

LOG_CONF = {
    'log_dir' : '/var/log/',
    'max_bytes' : 5000000,
    'backup_count' : 5,
}
