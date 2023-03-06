# -*- codeing = utf-8 -*-
# 中文乱码问题
# @Time : 2022-10-15 10:07
# @Author : 张杰
# @File :get_class.py
# @Software: PyCharm
import json
import re
import requests
from lxml import etree

import login
from remaining_number import get_num

cookies = login.login_vip()

# cookies = {
#     'cao_notice_cookie': '1',
#     'PHPSESSID': 'bdi0cg0o5hmiti4r50hu2vmgqb',
#     'wordpress_logged_in_40d7e158f587f1687f03728ca1a4c9bd': 'fqzjxgx%7C1665969401%7C580G9s1glwGr5AUeOBsY42grqzG5i7QC7O7R8RpV961%7C05eae47ef255fcfab745593b0a723b6b0c4301edc2ca37d4ea1a33478f1779e1',
# }


headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
}


# 获取课程的密码 "0":没有获取到密码，一般是百度网盘4位数的密码
def get_title_password(class_id):
    url = f'https://vipc9.com/{class_id}.html'
    print(f"正在获取\t{url}\t的标题和密码！")
    response = requests.get(url=url, cookies=cookies, headers=headers)
    data = {}
    if response.status_code == 200:
        page_text = response.text
        # with open(f"{class_id}.html", 'w', encoding='utf-8')as f:
        #     f.write(page_text)
        tree = etree.HTML(page_text)
        title = "".join(tree.xpath("/html/body/div[1]/div[2]/div[2]/section/div/header/h1/text()"))
        # print(title)
        try:
            password = "".join(re.findall("(\w{4})", "".join(tree.xpath('//*[@id="refurl"]/text()'))))
        except Exception as e:
            print(e)
        data['标题'] = title
        data['网盘密码'] = password
    else:
        print(f"获取网页失败！{response.status_code}")
    return data


# 课程对应的获取百度网盘地址
def get_url(class_id):
    params = {
        'post_id': class_id,
    }
    response = requests.get('https://vipc9.com/go', params=params, cookies=cookies, headers=headers)
    if response.status_code == 200:
        page_text = response.text
        # print(page_text)
        # with open(f"baidu_wangpan{class_id}.html", 'w', encoding='utf-8')as f:
        #     f.write(page_text)
        wang_pan_url = "".join(re.findall("window.location='(.*?)'", page_text))
        return wang_pan_url
    else:
        print(f"获取百度网盘链接失败！{response.status_code}")
        return None




def test1():
    with open("course_id.txt", 'r', encoding='utf-8') as f:
        class_id_list = f.readlines()
    number = 10
    while number > 3:
        if len(class_id_list) > 0:
            class_id = class_id_list[0].replace('\n', '')
        else:
            print("课程爬取完成！")
            break
        data = get_title_password(class_id)
        data['class_id'] = int(class_id)
        data['url'] = f"https://vipc9.com/{class_id}.html"
        data['网盘链接'] = get_url(class_id=class_id)
        if data['网盘链接'] != "":
            msg = f"{data['class_id']}\t{data['标题']}\t{data['url']}\t{data['网盘链接']}\t{data['网盘密码']}\n"
            print(msg)
            with open("vipc9.txt", 'a', encoding="utf-8")as f:
                f.write(msg)
            class_id_list.pop(0)
            with open("course_id.txt", 'w', encoding='utf-8')as f:
                f.writelines(class_id_list)
        else:
            print("获取链接失败！")
        print(data)
        number = get_num(cookies)
        print(f"当前剩余次数={number}")


if __name__ == '__main__':
    test1()
