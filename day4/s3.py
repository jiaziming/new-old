#!/usr/bin/python
# -*-coding:utf-8-*-


import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr


def mail(user):
    ret = True
    try:
        msg = MIMEText('邮件内容', 'plain', 'utf-8')
        msg['From'] = formataddr(["贾子明", 'wojiaojiaxiaoming@163.com'])
        msg['To'] = formataddr(["稍等", '739604412@qq.com'])
        msg['Subject'] = "主题"

        server = smtplib.SMTP("smtp.163.com", 25)
        server.login("wojiaojiaxiaoming@163.com", "asd920103")
        server.sendmail('wojiaojiaxiaoming@163.com', ['739604412@qq.com', ], msg.as_string())
        server.quit()
    except Exception:
        ret = False
    return ret


ret = mail('739604412@qq.com')
if ret:
    print('发送成功')
else:
    print('发送失败')

