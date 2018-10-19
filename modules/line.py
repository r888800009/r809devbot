from flask import Flask, request, abort
import config as cf

from linebot import (
    LineBotApi, WebhookHandler
)

from linebot.exceptions import (
    InvalidSignatureError
)

from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage
)

print("Start line api")
app = Flask(__name__)

lineBotaAPI = LineBotApi(cf.config["LineAPI"]["AccessToken"])
handler     = WebhookHandler(cf.config["LineAPI"]["Secret"])

@app.route("/linebot", methods = ['POST'])
def linebot():
    sign = request.headers['X-Line-Signature']

    body = request.get_data(as_text = True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, sign)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message = TextMessage)
def handle_message(event):
    lineBotaAPI.reply_message(
        event.reply_token,
        TextSendMessage(text = event.message.text))

app.run()
