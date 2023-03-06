import requests

token = "8d41c931c3e0403e895aabe49c3232d5"
url = f'http://www.pushplus.plus/send'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6307062c)"
}


# http://www.pushplus.plus/push1.html   官方网站
# 发推送消息到微信的pushplus公众号
def send_msg(title, content, template):
    data = {
        "token": token,
        'title': title,
        'content': content,
        'template': template,
    }
    response = requests.post(url=url, headers=headers, data=data)
    print(response.text)
    result = response.json()
    if result['code'] == 200:
        print(f'消息成功发送到pushplus微信公众号！')
    return result


def send_email_message():
    title = "这是邮件的标题"
    text = "这是邮件的正文"
    data = {
        "token": f"{token}",
        "title": title,
        "content": text,
        "channel": "mail",
        "webhook": "qq"
    }
    result = requests.post(url=url, data=data).text
    print(result)


if __name__ == '__main__':
    send_email_message()
