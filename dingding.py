# 请求的URL，WebHook地址
import json

import requests

webhook = "https://oapi.dingtalk.com/robot/send?access_token=6687a55083e0c5667a8532204d9d73c1331c82c3e1632cc28a3da60e233a428e"
#构建请求头部
header = {
        "Content-Type": "application/json",
        "Charset": "UTF-8"
    }

def push_to_dingding(text):
    tex = "天龙八部机器人："+text
    message = {
        "msgtype": "text",
        "text": {
            "content": tex
        },
        "at": {

            "isAtAll": True
        }

    }
    message_json = json.dumps(message)
    info = requests.post(url=webhook, data=message_json, headers=header)
    print(info.text)