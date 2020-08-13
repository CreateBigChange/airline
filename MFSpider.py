#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import time
import datetime
import smtplib
import smtplib
from email.mime.text import MIMEText
from email.header import Header



t=time.time();
timestamp = int(round(t * 1000));



hd = {'user-agent': 'Chrome/10'}
headers = {

# "Content-Length":"492",
# "Accept": "application/json, text/plain, */*",
# "Pragma": "no-cache",
# "Cache-Control": "no-cache",
# "Accept-Language":"zh-CN",
"User-Agent": " Chrome/84.0.4147.89"
# "Content-Type":"application/json;charset=UTF-8",
# "Origin": "https://www.xiamenair.com",
# "Sec-Fetch-Site": "same-origin",
# "Sec-Fetch-Mode": "cors",
# "Sec-Fetch-Dest":"empty",
# "Referer": "https://www.xiamenair.com/zh-cn/nticket.html?tripType=OW&orgCodeArr%5B0%5D=ICN&dstCodeArr%5B0%5D=XMN&orgDateArr%5B0%5D=2020-12-14&dstDate=&isInter=true&adtNum=1&chdNum=0&JFCabinFirst=false&acntCd=&mode=Money&partner=false&jcgm=false",
# "Accept-Encoding":"gzip, deflate, br",
# "Cookie":"gr_user_id=0394cfae-ec37-4ceb-9390-27132aee7349; sna=zh-cn; JSESSIONID=fb86d82d-8c8f-46ed-b9f8-2625a3dcfe6b; grwng_uid=4afcd8c1-2bfd-4231-bec4-6bbe7f3c4b49; c=HATfZnRV-1594968029240-b558188a62056452257123; _ga=GA1.2.1320399918.1594968029; _gid=GA1.2.1846454386.1594968029; BIGipServersvrpool_brandnew_9080=503317514.30755.0000; atk=undefined; userName=null; mfck=1; BIGipServersvrpool_brandnew_8080=1979712522.36895.0000; _fmdata=uquqKJeWbHnEmioavFDHTxEJHNg%2Fi37tydI2MVaVbOhIvKpL34td1%2Fk2Azoek5p4kZl%2FpGGFXOHWuPKS1caLxTAZvu6klKLxbEg5lQvZNk0%3D; _xid=ndj0%2BJmMCx%2FBOeZyFOcvMr2H%2BWqU8w2gzoIzPQaQHmJ%2BdkmKcvR63VHVuGufQsaGqX9yX7wQVtSWhD2erZnsuw%3D%3D; b014f44b281415f1_gr_session_id=c5f6add6-db63-460d-9bbe-0ab484f74822; b014f44b281415f1_gr_session_id_c5f6add6-db63-460d-9bbe-0ab484f74822=true"

}


str="https://www.xiamenair.com/zh-cn/nticket.html?tripType=OW&orgCodeArr%5B0%5D=ICN&dstCodeArr%5B0%5D=XMN&orgDateArr%5B0%5D=2020-12-13&dstDate=&isInter=true&adtNum=1&chdNum=0&JFCabinFirst=false&acntCd=&mode=Money&partner=false&jcgm=false"

requests.adapters.DEFAULT_RETRIES = 1





response = requests.get( str,headers=hd )  # post传参
response.encoding="utf-8"




print(response.text)





# 第三方 SMTP 服务
mail_host = "smtp.qq.com"  # 设置服务器
mail_user = "312479274@qq.com"  # 用户名
mail_pass = "lvmihqekwwxxbhfi"  # 口令


sender = '312479274@qq.com'
receivers = ['18390231902@163.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

#zhy.0908@gmail.com
#317153272@qq.com

message = MIMEText('南航已经出现经济舱，请点击链接进行购票处理', 'plain', 'utf-8')
message['From'] = Header("杨先圣", 'utf-8')
message['To'] = Header("yuanzhuang")

subject = '航班信息'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 587)  # 为 SMTP 端口号
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")

except smtplib.SMTPException:
    print("Error: 无法发送邮件")
