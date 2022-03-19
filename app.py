from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('BBgmOZWPy9FAbJqC91ykyShg7JORupShg1iwaYFP9a7fYgFyjIyJ+6l0/0Ow1vMfAyE86XyXhydh31URq5llM/nS+w+pzffgRkopXbCTpZjGluhRxNsQx789FaRkl/Av9ldlpiOZwyKYXlUbgurvRAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('558630c9d366711451019e6b479357b4')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    s = "你吃飯了嗎"
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=s))


if __name__ == "__main__":
    app.run()