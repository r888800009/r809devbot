# r809's bot
a bot inspired by [suntaidev](https://github.com/moontai0724/suntaidev)

It's maybe could chat with people or manage chat application group etc...
Um... but I hope it could make like a human that chat naturally.

## Dependents
``` bash
pip install flask   
pip install jieba 

# if you want to use line api
pip install line-bot-sdk

# if you want to use telegram api
pip install python-telegram-bot
```

## Installation and run
``` bash
# installation
git clone https://github.com/r888800009/r809devbot.git
cd r809devbot

# run
./main.py

# if you want to use line api
# and you want to use ngrok
ngrok http 127.0.0.1:5000
```

## Configure
``` Json
{
    "Output"  : [
        "LineAPI",
        "TelegramAPI"
    ],
    "SQL" : "sqlite",
    "LineAPI" : {
        "Path"        : "/linebot",
        "Secret"      : "",
        "AccessToken" : ""
    },
    "TelegramAPI" : {
        "Token" : ""
    }
}

```

### LineAPI
Configure `config.json`and only need to do chat with Line Chat account.

If your `Path` is `/linebot` and your domain is `example.com` then you
must to set your `Webhook URL` like `example.com/linebot`.

# For Developer
## Files
- `config.json`
- `main.py`
- *`chat.py` (unavailable)* for handle message
- `modules` directory, r809's bot is based on module design,
- `modules/line.py` Line API
- `modules/telegram.py` Telegram API 
- *`command.py` (unavailable)* Command System
so any command or plugin will put in here in principle.
- `database.sqlite` is database of r809's bot 
<!-- - `core` is a source code of core of r809's bot -->

## Configure
### config.json
There is  scheduled to support for the following connect configuration.
- [x] LineAPI
- [ ] Matrix
- [ ] IRC
- [x] Telegram API
- [ ] Messenger API
- [ ] REST
- [ ] ~~Minecraft Bukkit~~

Use these like below
``` Json
"Output"  : [
    "LineAPI",
    "Matrix",
    "IRC"
]
```

### chat.py
- `chat.handler(identifier, callback(message))` register a handler for handling received messages. 
- `chat.receive(identifier, message)` an interface for the module to receive messages from APIs.
- `chat.respond(identifier, callback(message))` an interface for the module responds messages to APIs.
- `chat.log(identifier, message)` log message to database.
<!-- - `chat.trigger()`-->

### command.py commands
- `disable message-print` do not show the message data when API receive
- `disable config dump` do not show the configure json when start
- `list config` show configure option
- `list config Output` show `Output` option
- `list config TelegramAPI.Token` show token of TelegramAPI


#### table 
``` sql
CREATE TABLE account (
    user_name,
    api_identifier,
    enable_api
);

```
