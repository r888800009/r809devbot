# r809's bot
a bot inspired by [suntaidev](https://github.com/moontai0724/suntaidev)

It's maybe could chat with people or manage chat application group etc...
Um... but I hope it could make like a human that chat naturally.

## Dependents
``` bash
pip install flask   

# if you want to use line api
pip install line-bot-sdk
```

## Installation and run
``` bash
# installation
git clone https://github.com/r888800009/r809devbot.git
cd r809devbot

# run
./main.py

# if you want to use ngrok
ngrok http 127.0.0.1:5000
```

## Configure
``` Json
{
    "Output"  : [
        "LineAPI"
    ],
    "SQL" : "sqlite",
    "LineAPI" : {
        "Path"        : "/linebot",
        "Secret"      : "",
        "AccessToken" : ""
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
- `modules` directory, r809's bot is based on module design,
so any command or plugin will put in here in principle.
- `database.sqlite` is database of r809's bot 
<!-- - `core` is a source code of core of r809's bot -->

## Configure
### config.json
There is  scheduled to support for the following connect configuration.
- [x] LineAPI
- [ ] Matrix
- [ ] IRC
- [ ] Telegram API
- [ ] Messenger API
- [ ] REST

Use these like below
``` Json
"Output"  : [
    "LineAPI",
    "Matrix",
    "IRC"
]
```
