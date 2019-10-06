import requests

url="http://106.ihuyi.com/webservice/sms.php?method=Submit"

account="C32937805"

password="afc0ccfec290f5c622cc8b6815dad51a"

mobile="18703980651"

content="黑，嘿嘿。"

headers = {
    "Content-type": "application/x-www-form-urlencoded",
    "Accept": "text/plain"
}
data = {
    "account": account,
    "password": password,
    "mobile": mobile,
    "content": content,
}

response = requests.post(url,headers = headers,data=data)

print(response.content.decode())