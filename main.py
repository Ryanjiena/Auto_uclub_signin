import os
import requests
import time
import schedule
from bs4 import BeautifulSoup

QMSG_KEY = os.environ["QMSG_KEY"]
PUSH_KEY = os.environ["PUSH_KEY"]
TELEGRAMBOT_TOKEN = os.environ["TELEGRAMBOT_TOKEN"]
TELEGRAMBOT_CHATID = os.environ["TELEGRAMBOT_CHATID"]

username = ""
password = ""

if(username == "", password == ""):
    username = input("账号:")
    password = input("密码:")

HEADERS = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66",
    "Host": "uclub.ucloud.cn"
}

# HEADERS = {
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
#                   "Chrome/86.0.4240.112 Safari/537.36",
#     "Host": "uclub.ucloud.cn"
# }


def login() -> (requests.session, int):
    url = "https://uclub.ucloud.cn/index/user/login.html"
    session = requests.Session()
    f = session.get(url, headers=HEADERS)
    soup = BeautifulSoup(f.text, 'html.parser')
    token = soup.find(attrs={"name": "__token__"})['value']
    data = {
        "__token__": token,
        "account": username,
        "password": password,
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
    send_message = 'https://api.telegram.org/bot' + TELEGRAMBOT_TOKEN + \
        '/sendMessage?chat_id=' + TELEGRAMBOT_CHATID + \
        '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_message)
    # print(response.json())


def qmsg_sendmessage(bot_message):
    send_message = 'https://qmsg.zendee.cn/send/' + QMSG_KEY + '?msg=' + bot_message
    response = requests.get(send_message)
    # print(response.json())

def qmsg_sendgroupmessage(bot_message):
    send_message = 'https://qmsg.zendee.cn/group/' + QMSG_KEY + '?msg=' + bot_message
    response = requests.get(send_message)
    # print(response.json())  

def sc_sendmessage(bot_title, bot_message):
    send_message = 'https://sc.ftqq.com/' + PUSH_KEY + \
        '.send?text=' + bot_title + '&desp=' + bot_message
    response = requests.get(send_message)
    # print(response.json())


if __name__ == '__main__':
    if not username or not password:
        print("你没有添加账户密码")
        exit(1)
    s = login()
    v_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    title = "UCloud Uclub 社区今日打卡情况"
    message = "\n\n - 打卡时间：" + v_time + "\n - 打卡用户：" + username + "\n"
    if not s:
        message = message + " - 打卡日志：登陆失败，请检查你的登录信息是否准确!" + "\n"
        print('')
        print('登陆失败!')
        message0 = title + message
    else:
        message = message + " - 打卡前积分为: %d" % (getCredit(s)) + "\n"
        print('')
        print('登陆成功!')
        signin(s)
        message = message + " - 打卡后积分为: %d" % (getCredit(s)) + "\n"
        print('签到完成!')
        message0 = title + message
    # TGBot 推送
    if TELEGRAMBOT_TOKEN and TELEGRAMBOT_CHATID:
        print('检测到 TGBot 配置信息，正在尝试 TGBot 推送')
        telegrambot_sendmessage(message0)
        # TGBot 推送结果分析
    # Qmsg 酱推送
    if QMSG_KEY:
        print('检测到 Qmsg 配置信息，正在尝试 Qmsg 酱推送')
        qmsg_sendmessage(message0)
        qmsg_sendgroupmessage(message0)
        # Qmsg 酱推送结果分析
    # Server 酱推送
    if PUSH_KEY:
        print('检测到 Server 配置信息，正在尝试 Server 酱推送')
        sc_sendmessage(title, message)
        # Server 酱推送结果分析
