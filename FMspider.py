import re
import requests
import time
import datetime
import smtplib

from email.mime.text import MIMEText
from email.header import Header

t=time.time();
timestamp = int(round(t * 1000));



headers = {

"Accept": "application/json, text/plain, */*",
"Accept-Encoding": "gzip, deflate, br",

"Accept-Language": "en-GB,en;q=0.9,en-US;q=0.8",
"Connection": "keep-alive",
"Content-Length": "223",

"Content-Type": "application/json;charset=UTF-8;",
"Cookie": "SESSION=06a9bcb2-3336-4219-b011-fa14798b9984; Webtrends=1eb3845f.5aa862f73cd25; language=zh_CN; _ga=GA1.2.1448629795.1594868185; _gid=GA1.2.1930866271.1594868185; user_ta_session_id=995e5938-f949-405c-a51f-2d22adf51db3; gr_user_id=24bd73e3-30d4-4038-bd7b-c80ffc6ec754; grwng_uid=4afcd8c1-2bfd-4231-bec4-6bbe7f3c4b49; HMF_CI=b8d7771212d463dfff6dacc7f07ad066aefce87f24dcadfa8f727b549685aba9b2; ceairWebType=new; _ga=GA1.3.1448629795.1594868185; _gid=GA1.3.1930866271.1594868185; CSH_DF=cnbg1OrtHd/P7UmgFztwOvEX0WzTfd/CUo/UdIHFEbX7HiLRU8SYqzysUXWNawq6Y2; _Jo0OQK=339012E32EE97601DDAA5E15195304CA712D65BFD96DC6118884C1791BB60A388626F85ECB60FF8D5BCE99CC29FE529492AED1A4593FACB0B4FCFD30CA11BA8B1323275CA6B8843FC1F71EB2AC03925AD4771EB2AC03925AD47DEBC77C68AE85A1EGJ1Z1Sw==; 84bb15efa4e13721_gr_session_id=1c12d4f6-1c76-48c6-8ea2-1e0bfdd6d2ab; 84bb15efa4e13721_gr_session_id_1c12d4f6-1c76-48c6-8ea2-1e0bfdd6d2ab=true; _pk_id.2.636f=deffd0312db841db.1594869342.3.1594879181.1594874941.",
"Host": "global.ceair.com",
"Origin": "https://global.ceair.com",
"Referer": "https://global.ceair.com/shopping?key=JTdCJTIydHJhdmVsVHlwZSUyMiUzQSUyMm9uZXdheSUyMiUyQyUyMnBhc3Nlbmdlck51bSUyMiUzQSUyMjElMkMwJTJDMCUyMiUyQyUyMmRlcENpdHklMjIlM0ElMjJTRUwlMjIlMkMlMjJhcnJDaXR5JTIyJTNBJTIyU0hBJTIyJTJDJTIyZGVwVmFsdWVzJTIyJTNBJTIySUNOJTJDR01QJTIyJTJDJTIyYXJyVmFsdWVzJTIyJTNBJTIyUFZHJTJDU0hBJTIyJTJDJTIyZGVwQ2l0eU5hbWUlMjIlM0ElMjIlRTklQTYlOTYlRTUlQjAlOTQlMjIlMkMlMjJhcnJDaXR5TmFtZSUyMiUzQSUyMiVFNCVCOCU4QSVFNiVCNSVCNyUyMiUyQyUyMmRlcFNlbGVjdFZhbHVlJTIyJTNBJTIySUNOJTIyJTJDJTIyYXJyU2VsZWN0VmFsdWUlMjIlM0ElMjJQVkclMjIlMkMlMjJkZXBMYWJlbCUyMiUzQSUyMiVFNCVCQiU4MSVFNSVCNyU5RCVFNSU5QiVCRCVFOSU5OSU4NSVFNiU5QyVCQSVFNSU5QyVCQSUyMiUyQyUyMmFyckxhYmVsJTIyJTNBJTIyJUU2JUI1JUE2JUU0JUI4JTlDJUU1JTlCJUJEJUU5JTk5JTg1JUU2JTlDJUJBJUU1JTlDJUJBJTIyJTJDJTIyaXNBcnJDaXR5JTIyJTNBZmFsc2UlMkMlMjJpc0RlcENpdHklMjIlM0FmYWxzZSUyQyUyMmFyckNuJTIyJTNBJTIyQ04lMjIlMkMlMjJkZXBDbiUyMiUzQSUyMktSJTIyJTJDJTIyZGF0ZSUyMiUzQSUyMjIwMjAtMTItMTElMjIlMkMlMjJjYWJpbkNsYXNzJTIyJTNBJTIyQUxMJTIyJTJDJTIycGF5V2F5JTIyJTNBJTIybW9uZXklMjIlMkMlMjJ0JTIyJTNBMTU5NDg3ODYxMDMyNSU3RA%3D%3DENCODEKEY",
"Sec-Fetch-Dest": "empty",
"Sec-Fetch-Mode": "cors",
"Sec-Fetch-Site": "same-origin",
"Shakehand": "9177f45cba47c0abcdb88d80d3d5982e",
"Site": "zh_CN",

"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"

}


data = {

"adultCount": 1,
"arrCityCode": "SHA",
"arrCode": "PVG",
"arrDate": "",
"cabinLevel": "",
"childCount": 0,
"depCityCode": "SEL",
"depCode": "ICN",
"depDate": "2020-12-11",
"deviceId": "",
"infantCount": 0,
"onlyPlaneFlag": "true",
"routeType": "OW"

}


str="https://global.ceair.com/self-service/before/flight-status?key=JTdCJTIycGFyYW0lMjIlM0ElMjIlN0IlNUMlMjJzZWFyY2hCeVdheSU1QyUyMiUzQSU1QyUyMmZsaWdodE5vJTVDJTIyJTJDJTVDJTIyZmxpZ2h0Tm8lNUMlMjIlM0ElNUMlMjJGTTg4NiU1QyUyMiUyQyU1QyUyMmRhdGUlNUMlMjIlM0ElNUMlMjIyMDIwLTA3LTE5JTVDJTIyJTdEJTIyJTdEENCODEKEY"

print(str)


response = requests.post( str , params=data,headers=headers )  # post传参


print(response.status_code)

text=response.text;
print(text)

status=re.match( r'<td class=\'flyGreen\' width=\'82\'>\"+status+\"</td><td class=\'flyGreen\' width=\'82\'>"+delayReasonOut+"</td>"(.*)  (.*?) .*', text, re.M|re.I)

if status==1:
    # send emial
    sender = 'from@runoob.com'
    receivers = ['429240967@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
    message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
    message['From'] = Header("菜鸟教程", 'utf-8')  # 发送者
    message['To'] = Header("测试", 'utf-8')  # 接收者

    subject = 'Python SMTP 邮件测试'
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP('localhost')
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")

    except smtplib.SMTPException:
        print("Error: 无法发送邮件")



