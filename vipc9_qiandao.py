# -*- codeing = utf-8 -*-
# 中文乱码问题
# @Time : 2023-01-02 10:56
# @Author : 张杰
# @File :vipc9_qiandao.py
# @Software: PyCharm
import time

import requests

from pushplus import send_msg
# cookies = {
#     'wordpress_40d7e158f587f1687f03728ca1a4c9bd': 'fqzjxgx%7C1672800326%7Cp5jqFpAcIykiLpUd0nyHfdKkVYq6UrpAPTr6d7nLV9h%7C929ee8672eb2daa3efc22a078e4b1e203d09e86a7cf32e495a2583f2c99408ea',
#     'cao_notice_cookie': '1',
#     'PHPSESSID': '7nmeu6m201sguc933b9l2l5ab0',
#     'wordpress_logged_in_40d7e158f587f1687f03728ca1a4c9bd': 'fqzjxgx%7C1672800326%7Cp5jqFpAcIykiLpUd0nyHfdKkVYq6UrpAPTr6d7nLV9h%7Cec9bbc1489a9a465f3a588cd23129af0d69a20964c0763bd7ceb110b59cc8a31',
# }
from vipc9_login import login_vip

headers = {
    'authority': 'vipc9.com',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'wordpress_40d7e158f587f1687f03728ca1a4c9bd=fqzjxgx%7C1672800326%7Cp5jqFpAcIykiLpUd0nyHfdKkVYq6UrpAPTr6d7nLV9h%7C929ee8672eb2daa3efc22a078e4b1e203d09e86a7cf32e495a2583f2c99408ea; cao_notice_cookie=1; PHPSESSID=7nmeu6m201sguc933b9l2l5ab0; wordpress_logged_in_40d7e158f587f1687f03728ca1a4c9bd=fqzjxgx%7C1672800326%7Cp5jqFpAcIykiLpUd0nyHfdKkVYq6UrpAPTr6d7nLV9h%7Cec9bbc1489a9a465f3a588cd23129af0d69a20964c0763bd7ceb110b59cc8a31',
    'origin': 'https://vipc9.com',
    'pragma': 'no-cache',
    'referer': 'https://vipc9.com/',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}


def user_qiandao(cookies):
    data = {
        'action': 'user_qiandao',
    }
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    response = requests.post('https://vipc9.com/wp-admin/admin-ajax.php', cookies=cookies, headers=headers, data=data)
    res_dict = response.json()
    msg = f"{now}\t{res_dict['msg']}\n"
    print(msg)
    with open("vipc9_qiandao.txt", 'a', encoding='utf-8')as f:
        f.write(msg)

    send_msg(f"vipc9-{res_dict['msg']}", msg, '')


if __name__ == '__main__':
    login_cookies = login_vip()
    user_qiandao(login_cookies)
