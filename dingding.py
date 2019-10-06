import json
import requests

url = "https://oapi.dingtalk.com/robot/send?access_token=b665c6e977b4ded24d9ef54e2811c2a1e0d2159a0bfd5fd53068267a5287b740"

headers = {
    "Content-Type": "application/json",
    "Charset": "utf-8"
}

requests_data = {
    "msgtype": "text",
    "text": {
        "content": "大傻yang！"
    },
    "at": {
        "atMobiles": ["廖阳"
        ],
        "isAtAll": False,
        "AtOne":["廖阳"]
    }
}
import time
while True:
    time.sleep(2)
    sendData = json.dumps(requests_data)

    response = requests.post(url = url,headers = headers, data = sendData)

    content = response.json()

    print(content)

