import smtplib
from email.mime.text import MIMEText

subject="老王说事"
content="""
 预知后事如何，且听下回分解
 """
sender="2686946878@qq.com"
recver="""827582114@qq.com,
646112954@qq.com,
2686946878@qq.com
 """

password="fweckgqzrfrvdehh"

message=MIMEText(content,"plain","utf-8")

message["Subject"]=subject
message["From"]=sender
message["To"]=recver

smtp=smtplib.SMTP_SSL("smtp.qq.com",465)
smtp.login(sender,password)
smtp.sendmail(sender,recver.split(",\n"),message.as_string())

smtp.close()