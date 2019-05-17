# -*- coding:utf-8 -*-
import os
from django.core.mail import EmailMultiAlternatives


os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

if __name__ == '__main__':

    subject, from_email, to = '来自localhost的测试邮件', '发送方邮箱', '接收方邮箱'
    text_content = '欢迎访问localhost！'
    html_content = '<p>欢迎访问<a href="http://127.0.0.1:8000" target=blank>127.0.0.1:8000</a>，' \
                   '本地登录界面！</p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()