"""modules for Line chat API"""
from flask import Flask, request, abort
import jieba

from linebot import (
    LineBotApi, WebhookHandler
)

from linebot.exceptions import (
    InvalidSignatureError
)

from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage
)

import config as cf

print("Start line api")
app = Flask(__name__)

lineBotaAPI = LineBotApi(cf.CONFIG["LineAPI"]["AccessToken"])
handler     = WebhookHandler(cf.CONFIG["LineAPI"]["Secret"])

@app.route(cf.CONFIG["LineAPI"]["Path"], methods = ['POST'])
def linebot():
    sign = request.headers['X-Line-Signature']

    body = request.get_data(as_text = True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, sign)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    seg_list = jieba.cut(event.message.text)
    lineBotaAPI.reply_message(
        event.reply_token,
        TextSendMessage(text=", ".join(seg_list)))

app.run()
