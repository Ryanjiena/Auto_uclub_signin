import os
import requests
import time
import schedule
from bs4 import BeautifulSoup

USERNAME = os.environ["USERNAME1"]
PASSWORD = os.environ["PASSWORD1"]
TELEGRAMBOT_TOKEN = os.environ["TELEGRAMBOT_TOKEN"]
TELEGRAMBOT_CHATID = os.environ["TELEGRAMBOT_CHATID"]

HEADERS = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/86.0.4240.112 Safari/537.36",
    "Host": "uclub.ucloud.cn"
}


def login() -> (requests.session, int):
    url = "https://uclub.ucloud.cn/index/user/login.html"
    session = requests.Session()
    f = session.get(url, headers=HEADERS)
    soup = BeautifulSoup(f.text, 'html.parser')
    token = soup.find(attrs={"name": "__token__"})['value']
    data = {
        "__token__": token,
        "account": USERNAME,
        "password": PASSWORD,
        "keeplogin": "1"
    }
    f = session.post(url, headers=HEADERS, data=data)
    f.raise_for_status()
    if f.text.find("登录成功") == -1:
        return None
    return session


def getCredit(session) -> int:
    url = "https://uclub.ucloud.cn/index/user/index.html"
    f = session.get(url, headers=HEADERS)
    soup = BeautifulSoup(f.text, 'html.parser')
    cred = int(soup.find('a', class_='viewscore').text)
    return cred


def signin(session):
    url = "https://uclub.ucloud.cn/index/signin/dosign.html"
    f = session.post(url)
    soup = BeautifulSoup(f.text, 'html.parser')
    print(soup.find('h1').text)


def telegrambot_sendmessage(bot_message):
    send_message = 'https://api.telegram.org/bot' + TELEGRAMBOT_TOKEN + '/sendMessage?chat_id=' + TELEGRAMBOT_CHATID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_message)
    print(response.json())


if __name__ == '__main__':
    if not USERNAME or not PASSWORD:
        print("你没有添加账户密码")
        exit(1)
    if not TELEGRAMBOT_TOKEN or not TELEGRAMBOT_CHATID:
        print("你没有配置 TelegramBot")
        exit(1)
    s = login()
    v_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
    message0 = "UCloud Uclub 社区今日打卡情况：\n\n - 打卡时间：" + v_time + "\n - 打卡用户：" + USERNAME + "\n"
    if not s:
        message1 = " - 打卡日志：登陆失败，请检查你的登录信息是否准确!" + "\n"
        message = message0 + message1
        telegrambot_sendmessage(message)
        exit(1)
    else:
        message1 = " - 打卡前积分为: %d"%(getCredit(s)) + "\n"
        print('登陆成功，您目前的积分为: %d' % getCredit(s))
        signin(s)
        message2 = " - 打卡后积分为: %d"%(getCredit(s)) + "\n"
        print('签到完成，您目前的积分为: %d' % getCredit(s))
        message = message0 + message1 + message2
        telegrambot_sendmessage(message)
