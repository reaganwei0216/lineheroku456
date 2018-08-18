# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 01:00:17 2018

@author: linzino
"""


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

line_bot_api = LineBotApi('YRaJWT3R9MTO0qk6hpSHMzusdU5/cCnoTIy7gCTYAEfbbAfjN8QdRznang4ERIS03BfVSfMF37za8fqrG2cQCvk8B/m4bRJhnFZR5zcQb6iv/ofasR39HAbLso8kUyrZacvEBY2guF+4KVSjDGbZLgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('e78f5e3f5bf5205553c1bcddebad932d')



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
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    string=''
    if msg=="A":
        string='AAA'
    else:
        string='BBB'
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text=string))
  
 

if __name__ == '__main__':
    app.run(debug=True)
