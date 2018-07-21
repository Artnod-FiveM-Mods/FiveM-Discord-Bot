#!/usr/bin/python3
#-*- coding: utf-8 -*-
'''
Created on 10 avr. 2018

@author: artnod
'''
import sys, datetime, time, json, requests, socket, logging
from collections import defaultdict
from settings import WEBHOOK_CONF

class Webhook:
    def __init__(self, url, **kwargs):
        """
        Initialise a Webhook Embed Object
        """
        self.logger = logging.getLogger('discord_hook.Webhook')
        self.logger.debug('Init a Webhook object')
        self.url = url 
        self.msg = kwargs.get('msg')
        self.color = kwargs.get('color')
        self.title = kwargs.get('title')
        self.title_url = kwargs.get('title_url')
        self.author = kwargs.get('author')
        self.author_icon = kwargs.get('author_icon')
        self.author_url = kwargs.get('author_url')
        self.desc = kwargs.get('desc')
        self.fields = kwargs.get('fields', [])
        self.image = kwargs.get('image')
        self.thumbnail = kwargs.get('thumbnail')
        self.footer = kwargs.get('footer')
        self.footer_icon = kwargs.get('footer_icon')
        self.ts = kwargs.get('ts')
    
    def add_field(self,**kwargs):
        '''
        Adds a field to `self.fields`
        '''
        self.logger.debug(sys._getframe().f_code.co_name)  
        name = kwargs.get('name')
        value = kwargs.get('value')
        inline = kwargs.get('inline', True)
        field = {
            'name' : name,
            'value' : value,
            'inline' : inline
        }
        self.fields.append(field)
    
    def set_desc(self,desc):
        '''
        Set description
        '''
        self.logger.debug(sys._getframe().f_code.co_name)   
        self.desc = desc
    
    def set_author(self, **kwargs):
        '''
        Set author
        '''
        self.logger.debug(sys._getframe().f_code.co_name)    
        self.author = kwargs.get('name')
        self.author_icon = kwargs.get('icon')
        self.author_url = kwargs.get('url')
    
    def set_title(self, **kwargs):
        '''
        Set title
        '''
        self.logger.debug(sys._getframe().f_code.co_name)  
        self.title = kwargs.get('title')
        self.title_url = kwargs.get('url')
    
    def set_thumbnail(self, url):
        '''
        Set thumbnail
        '''
        self.logger.debug(sys._getframe().f_code.co_name)  
        self.thumbnail = url
    
    def set_image(self, url):
        '''
        Set image
        '''
        self.logger.debug(sys._getframe().f_code.co_name)   
        self.image = url
    
    def set_footer(self,**kwargs):
        '''
        Set footer
        '''
        self.logger.debug(sys._getframe().f_code.co_name)  
        self.footer = kwargs.get('text')
        self.footer_icon = kwargs.get('icon')
        ts = kwargs.get('ts')
        if ts == True:
            self.ts = str(datetime.datetime.utcfromtimestamp(time.time()))
        else:
            self.ts = str(datetime.datetime.utcfromtimestamp(ts))
    
    def del_field(self, index):
        '''
        Delete field
        '''
        self.logger.debug(sys._getframe().f_code.co_name)  
        self.fields.pop(index)
    
    @property
    def json(self,*arg):
        '''
        Formats the data into a payload
        '''
        self.logger.debug(sys._getframe().f_code.co_name)  
        data = {}
        data["embeds"] = []
        embed = defaultdict(dict)
        if self.msg: data["content"] = self.msg
        if self.author: embed["author"]["name"] = self.author
        if self.author_icon: embed["author"]["icon_url"] = self.author_icon
        if self.author_url: embed["author"]["url"] = self.author_url
        if self.color: embed["color"] = self.color 
        if self.desc: embed["description"] = self.desc 
        if self.title: embed["title"] = self.title 
        if self.title_url: embed["url"] = self.title_url 
        if self.image: embed["image"]['url'] = self.image
        if self.thumbnail: embed["thumbnail"]['url'] = self.thumbnail
        if self.footer: embed["footer"]['text'] = self.footer
        if self.footer_icon: embed['footer']['icon_url'] = self.footer_icon
        if self.ts: embed["timestamp"] = self.ts 
        if self.fields:
            embed["fields"] = []
            for field in self.fields:
                f = {}
                f["name"] = field['name']
                f["value"] = field['value']
                f["inline"] = field['inline'] 
                embed["fields"].append(f)
        data["embeds"].append(dict(embed))
        empty = all(not d for d in data["embeds"])
        if empty and 'content' not in data:
            print('You cant post an empty payload.')
        if empty: data['embeds'] = []
        return json.dumps(data, indent=4)
    
    def post(self):
        """
        Send the JSON formated object to the specified `self.url`.
        """
        self.logger.debug(sys._getframe().f_code.co_name)  
        headers = {'Content-Type': 'application/json'}
        result = requests.post(self.url, data=self.json, headers=headers)
        if result.status_code == 400:
            self.logger.err("Post Failed, Error 400")
        else:
            self.logger.info("Payload delivered successfuly - Code : "+str(result.status_code))

class CheckPorthook:
    def __init__(self, hostname, port, servername, webhook_url):
        """
        Initialise a fivem Webhook
        """
        self.logger = logging.getLogger('discord_hook.CheckPorthook')
        self.logger.debug('Init a CheckPorthook object')
        self.hostname = hostname
        self.port = port
        self.servername = servername
        self.webhook_url = webhook_url
        self.lastState = False
    
    def isRunning(self):
        """
        Check if Port is open
        """
        self.logger.debug(sys._getframe().f_code.co_name)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((self.hostname, self.port))
        if result == 0:
                self.logger.debug('Check server on {}:{} - Success'.format(self.hostname, self.port))
                self.running = True
        else:
            self.logger.debug('Check server on {}:{} - Failed'.format(self.hostname, self.port))
            self.running = False
    
    def sendState(self):
        """
        Send server state
        """
        self.logger.debug(sys._getframe().f_code.co_name)
        embed = Webhook(self.webhook_url, color=123123)
        embed.set_author(name=WEBHOOK_CONF['message']['author'], icon=WEBHOOK_CONF['message']['author_icon'])
        if self.running == True:
            self.logger.info('{}:{} is available'.format(self.hostname, self.port))
            embed.set_desc('{} is available!'.format(self.servername))
            embed.add_field(name='Hostname',value=self.hostname)
            embed.add_field(name='Port',value=self.port)
            embed.set_thumbnail(WEBHOOK_CONF['message']['thumbnail_on'])
            embed.set_footer(text='Good Game',icon=WEBHOOK_CONF['message']['footer'],ts=True)
        else:
            self.logger.info('{}:{} is unavailable'.format(self.hostname, self.port))
            embed.set_desc('{} is unavailable!'.format(self.servername))
            embed.set_thumbnail(WEBHOOK_CONF['message']['thumbnail_off'])
            embed.set_footer(text='See you later',icon=WEBHOOK_CONF['message']['footer'],ts=True)
        embed.post()
    
    def process(self):
        """
        If server status change
        Then send server new state
        """
        self.logger.debug(sys._getframe().f_code.co_name)  
        self.isRunning()
        if self.running != self.lastState:
            self.sendState()
            self.lastState = self.running
        