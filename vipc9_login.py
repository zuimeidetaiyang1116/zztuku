# -*- codeing = utf-8 -*-
# 中文乱码问题
# @Time : 2022-10-15 16:58
# @Author : 张杰
# @File :vipc9_login.py
# @Software: PyCharm
import requests

cookies = {
    'cao_notice_cookie': '1',
    'PHPSESSID': '4ptjpekniop57h018jbor17trp',
    'wordpress_test_cookie': 'WP%20Cookie%20check',
}


def login_vip():
    headers = {
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
    }

    data = 'action=user_login&username=fqzjxgx&password=fqzjxgx'
    session = requests.session()
    response = session.post('https://vipc9.com/wp-admin/admin-ajax.php', cookies=cookies, headers=headers, data=data)
    # print(response)

    login_cookies = response.cookies.get_dict()
    # print(login_cookies)
    if response.status_code == 200:
        page_text = response.text
        # print(page_text)
        # with open("login.html", 'w', encoding='utf-8')as f:
        #     f.write(page_text)
    else:
        print("获取登录页面失败", response)
    return login_cookies




if __name__ == '__main__':
    login_cookies = login_vip()
    print(login_cookies)
