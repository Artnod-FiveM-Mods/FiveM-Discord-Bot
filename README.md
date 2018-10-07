# FiveM-Discord-Bot
Simple Discord Bot/Webhook for fivem linux server.  

**Features WebHook:**
```
Send message when server state changed.
```

**Features Bot:**
```
A simple Bot to start/stop/update fivem server

​Categories:
  update     Update a specific resource
  help   Shows this message.
  stop       Stop a specific server
  start      Start a specific server

Type /help command for more info on a command.
You can also type /help category for more info on a category.
```

## Install
```
wget https://raw.githubusercontent.com/Artnod-FiveM-Mods/FiveM-Discord-Bot/master/bootstrap/bootstrap.sh
chmod +x bootstrap.sh
./bootstrap.sh -i
```  
## Install Webhook (Windows only)
```
Need python3
Need ``lxml`` python package ``pip install lxml``
```  
## Config
Edit `/usr/local/bin/fivembot/settings.py` with your settings.  

### Bot Config
```python
BOT_CONF = {
    'bot_token' : '<token>',
    'bot_channel' : '<channel>',
    'bot_admin_list' : ('<user>',),
}
```
Replace **\<token>** by bot token  
Replace **\<channel>** by a channel using by bot  
Replace **\<user>** by id from allowed users. Can add many users `('<user_1_ID>', '<user_2_ID>')`  

### Hook Config  
```python
WEBHOOK_CONF = {
    'webhook_url' : '<webhook_url>',
}
```
Replace **\<webhook_url>** by webhook url  

### Fivem Config  
```python
FIVEM_CONF = {
    'server_name' : '<server name>',
    'server_port' : 30120,
}
```
Replace **\<server name>** by your server name  
