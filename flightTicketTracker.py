from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import time
import requests
from playsound import playsound
import re
from io import BytesIO
from zipfile import ZipFile
import smtplib

from email.mime.text import MIMEText
from email.header import Header

####################################################################################################

runtime = 5  # total runtime for this code flight_infoin minutes
frequency = 1  # frequency of search in minutes
exsit_flight=[]


way_of_notification = "alarm"  # call alarm / notify

sound_file = "./sound.mp3"
TIMEOUT_IN_SECONDS = 10  # set the time to wait till web fully loaded

EVENT_NAME = "UA857"

#周一 ['2020-10-19','2020-10-26']
#周二['2020-10-20','2020-10-27']
#周三['2020-10-21','2020-10-28']
#周四['2020-10-22','2020-10-29']
#周五['2020-10-16','2020-10-23','2020-10-30']
#周六['2020-10-17','2020-10-24','2020-10-31']
#周日['2020-10-18','2020-10-26','2020-11-1']

flight_info = {

    #行程不再有效
    '东航：MU5042 ICN-PVG 周五': {

        'search_dates': ['2020-10-16','2020-10-23','2020-10-30'],
        'base_url':'https://www.google.com.hk/flights?gl=tw#flt=ICN.PVG.2020-09-18.ICNPVG0MU5042;c:TWD;e:1;a:MU;sd:1;t:b;tt:o;sp:.TWD.'
    },

    #疫情原因 已经停运
    '国航： CA124 ICN-TAO 周五': {

        'search_dates': ['2020-10-16','2020-10-23','2020-10-30'],
        'base_url': 'https://www.google.com.hk/flights?gl=tw#flt=ICN.TAO.2020-08-14;c:TWD;e:1;a:CA;sd:1;t:f;tt:o'
    },

    '南航： CZ682 ICN-SHE 周日': {

        'search_dates': ['2020-10-18','2020-10-26','2020-11-1'],
        'base_url': 'https://www.google.com.hk/flights?gl=tw#flt=ICN.SHE.2020-06-13.ICNSHE0CZ682;c:TWD;e:1;a:CZ;sd:1;t:b;tt:o;sp:0.TWD.8867'
    },

    #疫情原因 已经停运
    '厦航：MF872 ICN-XMN 周一': {

        'search_dates': ['2020-10-19','2020-10-26'],
        'base_url': 'https://www.google.com.hk/flights?gl=tw#flt=ICN.XMN.2020-09-28;c:TWD;e:1;a:MF;sd:1;t:f;tt:o'
    },

    '山东航空： SC4088 ICN-TAO 周五': {

        'search_dates': ['2020-10-16','2020-10-23','2020-10-30'],
        'base_url': 'https://www.google.com.hk/flights?gl=tw#flt=ICN.TAO.2020-12-19.ICNTAO0SC4088;c:TWD;e:1;a:SC;sd:1;t:b;tt:o;sp:0.TWD.9707'
    },

    '青岛航空：QW9902 ICN-TAO 周六': {

        'search_dates': ['2020-10-17','2020-10-24','2020-10-31'],
        'base_url': 'https://www.google.com.hk/flights?gl=tw#flt=ICN.TAO.2020-08-29.ICNTAO0QW9902;c:TWD;e:1;a:QW;sd:1;t:b;tt:o;sp:.TWD.'
    },

    '大韩： KE832 ICN-SHE 周五': {

        'search_dates': ['2020-10-16','2020-10-23','2020-10-30'],
        'base_url': 'https://www.google.com.hk/flights?gl=tw#flt=ICN.SHE.2020-05-04.ICNSHE0KE832;c:TWD;e:1;a:KE;sd:1;t:b;tt:o;sp:0.TWD.8059'
    },

    '韩亚：OZ303 ICN-CGQ 周日': {

        'search_dates': ['2020-10-18','2020-10-26','2020-11-1'],
        'base_url': 'https://www.google.com.hk/flights?gl=tw#flt=ICN.CGQ.2020-04-11.ICNCGQ0OZ303;c:TWD;e:1;a:OZ;sd:1;t:b;tt:o;sp:0.TWD.6084'
    },

    '国航CA930 NRT-PVG 周四': {

        'search_dates': ['2020-10-22','2020-10-29'],
        'base_url': 'https://www.google.com.hk/flights?gl=tw#flt=NRT.PVG.2020-05-18;c:TWD;e:1;a:CA;sd:1;t:f;tt:o'
    },

    '厦航 MF810 NRT-FOC 周五': {

        'search_dates': ['2020-10-16','2020-10-23','2020-10-30'],
        'base_url': 'https://www.google.com.hk/flights?gl=tw#flt=NRT.FOC.2020-08-17.NRTFOC0MF810;c:TWD;e:1;a:MF;sd:1;t:b;tt:o;sp:0.TWD.78589'
    },

    '东航 MU524 NRT-PVG 周五': {

        'search_dates': ['2020-10-16','2020-10-23','2020-10-30'],
        'base_url': 'https://www.google.com.hk/flights?gl=tw#flt=NRT.PVG.2020-12-18.NRTPVG0MU524;c:TWD;e:1;a:MU;sd:1;t:b;tt:o;sp:.TWD.'
    },

    '南航 CZ628 NRT-SHE 周四': {

        'search_dates': ['2020-10-22','2020-10-29'],
        'base_url': 'https://www.google.com.hk/flights?gl=tw#flt=NRT.SHE.2020-12-17.NRTSHE0CZ628;c:TWD;e:1;a:CZ;sd:1;t:b;tt:o;sp:0.TWD.47150'
    },

    '上航 FM886 KUL-PVG 周日': {

        'search_dates': ['2020-10-18','2020-10-26','2020-11-1'],
        'base_url': 'https://www.google.com.hk/flights?gl=tw#flt=KUL.PVG.2020-12-20.KULPVG0FM886;c:TWD;e:1;a:FM;sd:1;t:b;tt:o;sp:0.TWD.23588'
    },

    '南航 CZ350 KUL-CAN 周二': {

        'search_dates': ['2020-10-20','2020-10-27'],
        'base_url': 'https://www.google.com.hk/flights?gl=tw#flt=KUL.PVG.2020-12-20.KULPVG0FM886;c:TWD;e:1;a:FM;sd:1;t:b;tt:o;sp:0.TWD.23588'
    },

    '南航 CZ348 CDG-CAN 周二': {

        'search_dates':['2020-10-20','2020-10-27'],
        'base_url': 'https://www.google.com.hk/flights?gl=tw#flt=KUL.CAN.2020-12-22.KULCAN0CZ348;c:TWD;e:1;a:CZ;sd:1;t:b;tt:o;sp:0.TWD.33734'
    },


    # 疫情原因 已经停运
    '国航 CA934 CDG-TSN 周三': {

        'search_dates': ['2020-10-21','2020-10-28'],
        'base_url': 'https://www.google.com.hk/flights?gl=tw#flt=CDG.TSN.2020-03-17;c:TWD;e:1;a:CA;sd:1;t:f;tt:o'
    },

    '东航 MU772 AMS-PVG 周一': {

        'search_dates': ['2020-10-19','2020-10-26'],
        'base_url': 'https://www.google.com.hk/flights?gl=tw#flt=AMS.PVG.2020-03-15.AMSPVG0MU772;c:TWD;e:1;a:MU;sd:1;t:b;tt:o;sp:.TWD.'
    },

    '南航 CZ308 AMS-CAN 周五': {

        'search_dates': ['2020-10-16','2020-10-23','2020-10-30'],
        'base_url': 'https://www.google.com.hk/flights?gl=tw#flt=AMS.CAN.2020-03-19.AMSCAN0CZ308;c:TWD;e:1;a:CZ;sd:1;t:b;tt:o;sp:0.TWD.64958'
    },



    '厦航 MF812 AMS-XMN 周三': {

        'search_dates': ['2020-10-21','2020-10-28'],
        'base_url': 'https://www.google.com.hk/flights?gl=tw#flt=AMS.XMN.2020-03-17.AMSPEK0KL897~PKXXMN1MF812;c:TWD;e:1;a:MF;sd:1;t:b;tt:o;sp:0.TWD.31881'
    },


    '东航 MU220 FRA-PVG 周二': {

        'search_dates': ['2020-10-20','2020-10-27'],
        'base_url': 'https://www.google.com.hk/flights?gl=tw#flt=FRA.PVG.2020-10-28.FRAPVG0MU220;c:TWD;e:1;a:MU;sd:1;t:b;tt:o;sp:.TWD.'
    },

    '东航 MU570 CDG-PVG 周日': {

        'search_dates': ['2020-10-18','2020-10-26','2020-11-1'],
        'base_url': 'https://www.google.com.hk/flights?gl=tw#flt=CDG.PVG.2020-03-14.CDGPVG0MU570;c:TWD;e:1;a:MU;sd:1;t:b;tt:o;sp:.TWD.'
    },


    # 疫情原因 已经停运
    '国航 CA936 FRA-PVG 周六': {

        'search_dates': ['2020-10-17','2020-10-24','2020-10-31'],
        'base_url': 'https://www.google.com.hk/flights?gl=tw#flt=FRA.PVG.2020-08-08;c:TWD;e:1;a:CA;sd:1;t:f;tt:o'
    },

    # 疫情原因 已经停运
    '国航 CA908 MAD-TSN 周六': {

        'search_dates': ['2020-10-17','2020-10-24','2020-10-31'],
        'base_url': 'https://www.google.com.hk/flights?gl=tw#flt=MAD.TSN.2020-06-05;c:TWD;e:1;a:CA;sd:1;t:f;tt:o'
    },


    'Delta DL287 SEA-PVG 周四': {

        'search_dates': ['2020-10-22','2020-10-29'],
        'base_url': 'https://www.google.com.hk/flights?hl=en&gl=am#flt=SEA.PVG.2020-11-27.SEAPVG0DL287;c:USD;e:1;s:0;a:DL;sd:1;t:b;tt:o;sp:2.USD.536510'
    },


    'Dleta DL283 DTW-PVG 周五': {

        'search_dates': ['2020-10-16','2020-10-23','2020-10-30'],
        'base_url': 'https://www.google.com.hk/flights?hl=en&gl=am#flt=SEA.PVG.2020-11-27.SEAPVG0DL283;c:USD;e:1;s:0;a:DL;sd:1;t:b;tt:o;sp:2.USD.536510'
    },

    'United UA857 SFO-PVG 周三、周六': {

        'search_dates':['2020-10-21','2020-10-28','2020-10-17','2020-10-24','2020-10-31'],
        #'base_url': 'https://www.google.com/flights?hl=en#flt=SFO.PVG.2020-11-26.SFOPVG0UA857;c:USD;e:1;s:0;sd:1;t:b;tt:o;sp:2.USD.706410'
        'base_url':'https://www.google.com.hk/flights?hl=en&gl=am#flt=SFO.PVG.2020-11-26.SFOPVG0UA857;c:USD;e:1;s:0;sd:1;t:b;tt:o;sp:2.USD.706410'
    },

    '济州航空 7C8501 ICN-WEH 周三': {

        'search_dates': ['2020-10-21','2020-10-28'],

        'base_url': 'https://www.google.com.hk/flights#flt=ICN.WEH.2020-10-14;c:HKD;e:1;a:7C;sd:1;t:f;tt:o',
    },


}

#####################################################################################################

API_KEY = open(r"API_KEY").readline().strip("\n")
if not API_KEY:
    raise Exception("You need to fill in the API_KEY in the directory.")


def get_web_driver():
    import platform

    print("downloading the web driver...", end="")

    system_name = platform.system()
    if system_name == "Windows":
        system_name = "win32"
    elif system_name == "Darwin":
        system_name = "mac64"
    elif system_name == "Linux":
        system_name = "linux64"
    else:
        raise Exception("Unknown system type")

    drive_url = f"https://chromedriver.storage.googleapis.com/86.0.4240.22/chromedriver_{system_name}.zip"

    response = requests.get(drive_url)
    response.raise_for_status()
    print(response.text)
    with ZipFile(BytesIO(response.content)) as z:
        z.extractall()

    print("Done")


def alarm(n):
    """repeat alarm sound for n times"""
    for i in range(n):
        playsound(sound_file)
        time.sleep(2)


def notify(*values):
    """
    use IFTTT to notify
    Refer to https://zhuanlan.zhihu.com/p/103419701 for details
    """
    data = {"value"+str(i+1): value for i, value in enumerate(values[:3])}

    response = requests.request("POST", data=data)
    response.raise_for_status()


def search(freq):
    for route, info in flight_info.items():

        print('开始搜索######### '+route+'#################################################')
        for date in info['search_dates']:

            url = re.sub(r"2020(-\d{2}){2}", date, info['base_url'])
            driver = webdriver.Chrome()
            driver.get(url)
            time.sleep(TIMEOUT_IN_SECONDS)  # Let the user actually see something!

            try:

                error_msg = driver.find_element_by_css_selector('.gws-flights-results__error-message')

            # jAEhX
            # flt - headline6

            except Exception:
                try:
                    cov_msg   =driver.find_element_by_css_selector('.jAEhX')
                    if cov_msg:
                        print(route+'时间：'+date+'   '+url+'航班受疫情影响 取消')
                        continue;
                except Exception:
                    print('')
                if way_of_notification == "alarm":

                   #alarm(3)

                   if (url in exsit_flight):
                        print(url+'航班已被标记')
                   else:
                       exsit_flight.append(url)
                       # 第三方 SMTP 服务
                       mail_host = "smtp.qq.com"  # 设置服务器
                       mail_user = "312479274@qq.com"  # 用户名
                       mail_pass = "orfddreacpbzbieb"  # 口令

                       sender = '312479274@qq.com'
                       receivers1 = ['18390231902@163.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
                       receivers2 = ['317153272@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
                       receivers3 = ['zhy.0908@gmail.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
                       receivers4 = ['312479274@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

                       message = MIMEText(route+'已经出现经济舱，请点击链接进行购票处理' + url, 'plain', 'utf-8')
                       message['From'] = Header("杨先圣", 'utf-8')
                       message['To'] = Header("yuanzhuang", 'utf-8')

                       subject = '航班信息'
                       message['Subject'] = Header(subject, 'utf-8')

                       try:
                           smtpObj = smtplib.SMTP()
                           smtpObj.connect(mail_host, 587)  # 为 SMTP 端口号
                           smtpObj.login(mail_user, mail_pass)
                           smtpObj.sendmail(sender, receivers1, message.as_string())
                           # smtpObj.sendmail(sender, receivers2, message.as_string())
                           # smtpObj.sendmail(sender, receivers3, message.as_string())
                           smtpObj.sendmail(sender, receivers4, message.as_string())
                           print(url+"邮件发送成功")
                       except smtplib.SMTPException:
                           print("Error: 无法发送邮件")

                       break;

                   time.sleep(2)

                elif way_of_notification == "notify":
                    notify(route)


                continue
            else:
                if len(error_msg.text):
                    print('flight search {} attempted on date {}, no result'.format(route, date))
                    driver.quit()

    time.sleep(freq*60)


if __name__ == '__main__':
    try:
        webdriver.Chrome().quit()
    except (FileNotFoundError, WebDriverException):
        get_web_driver()


    total_time = int(runtime / frequency)
    for _ in range(total_time):
        search(frequency)

