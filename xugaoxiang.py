# -*- codeing = utf-8 -*-
# 中文乱码问题
# @Time : 2022-12-28 9:33
# @Author : 张杰
# @File :qiandao.py
# @Software: PyCharm
import re
import datetime
import requests
from lxml import etree
from pushplus import send_msg

cookies = {
    'PHPSESSID': 'k6oo97v8lhia5cu7cd0ud8for2',
    '__bid_n': '1856b9f7673c0769184207',
    'FEID': 'v10-6569e6c7805f4b8ec90128ba9729ccb7fc36016e',
    '__xaf_fpstarttimer__': '1672547891115',
    '__xaf_ths__': '{"data":{"0":1,"1":43200,"2":60},"id":"c7e229cd-41a0-410a-bdcd-76da4437f43e"}',
    '__xaf_thstime__': '1672547891122',
    'Hm_lvt_36d091ca4167858e40c7bf39f954e3f9': '1672547891',
    'FPTOKEN': 'VD/OOmXoxam0vwZJMWGqA+Qc8y1qIKZ1PkwS2egSiCt02SCOzvxfCOsgAMknONXxLbm/sBGDy07pR+3pFBKm4JIqI1iWgj6IQCusM5IRHC3ZHlYsi+hRch3kffFwZD1jTJebVK/JGLY/A7sAjgk0oZVe1cja/sHF+ItIb/DBXrUyn1/zUVd5M7ncGrGSjqIRCyCZFeSAgSCo/N8WqkQobsBS7Vqln5wiAjhiVn3DilelulbypRSZQiHvWRZKafwwFYDi/HhdfqrKzn43Vq46uvWssfcqrbLG0SqQKNJ+X9SldR/hlLFI59S/w0EzI3GNFEe9zyLwvVk3clxxEEw6xKshbqJgG5aJ+f0B9J+7ClewE0yo2Cl0sLNLIooJDB/JPNRPDAUF7mUtS4h34mY9Bw==|Tqzg1fu5lG2YrgT017RatM3827ZcZB6uU4t9+rgPDv4=|10|8caeba33d08a89fe985c4d37a8261cf4',
    '__xaf_fptokentimer__': '1672547891185',
    'BAIDU_SSP_lcr': 'https://graph.qq.com/oauth2.0/show?which=Login&display=pc&response_type=code&client_id=101393123&redirect_uri=https%3A%2F%2Fwww.zztuku.com%2Foauth-callback-qq.html&state=&scope=get_user_info&display=default',
    'Hm_lpvt_36d091ca4167858e40c7bf39f954e3f9': '1672547986',
}

headers = {
    'authority': 'www.zztuku.com',
    # 'content-length': '0',
    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    'origin': 'https://www.zztuku.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.zztuku.com/',
    'accept-language': 'zh-CN,zh;q=0.9',
    # 'cookie': 'PHPSESSID=k6oo97v8lhia5cu7cd0ud8for2; __bid_n=1856b9f7673c0769184207; FEID=v10-6569e6c7805f4b8ec90128ba9729ccb7fc36016e; __xaf_fpstarttimer__=1672547891115; __xaf_ths__={"data":{"0":1,"1":43200,"2":60},"id":"c7e229cd-41a0-410a-bdcd-76da4437f43e"}; __xaf_thstime__=1672547891122; Hm_lvt_36d091ca4167858e40c7bf39f954e3f9=1672547891; FPTOKEN=VD/OOmXoxam0vwZJMWGqA+Qc8y1qIKZ1PkwS2egSiCt02SCOzvxfCOsgAMknONXxLbm/sBGDy07pR+3pFBKm4JIqI1iWgj6IQCusM5IRHC3ZHlYsi+hRch3kffFwZD1jTJebVK/JGLY/A7sAjgk0oZVe1cja/sHF+ItIb/DBXrUyn1/zUVd5M7ncGrGSjqIRCyCZFeSAgSCo/N8WqkQobsBS7Vqln5wiAjhiVn3DilelulbypRSZQiHvWRZKafwwFYDi/HhdfqrKzn43Vq46uvWssfcqrbLG0SqQKNJ+X9SldR/hlLFI59S/w0EzI3GNFEe9zyLwvVk3clxxEEw6xKshbqJgG5aJ+f0B9J+7ClewE0yo2Cl0sLNLIooJDB/JPNRPDAUF7mUtS4h34mY9Bw==|Tqzg1fu5lG2YrgT017RatM3827ZcZB6uU4t9+rgPDv4=|10|8caeba33d08a89fe985c4d37a8261cf4; __xaf_fptokentimer__=1672547891185; BAIDU_SSP_lcr=https://graph.qq.com/oauth2.0/show?which=Login&display=pc&response_type=code&client_id=101393123&redirect_uri=https%3A%2F%2Fwww.zztuku.com%2Foauth-callback-qq.html&state=&scope=get_user_info&display=default; Hm_lpvt_36d091ca4167858e40c7bf39f954e3f9=1672547986',
}


now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")


def get_qiandao_info():
    response = requests.post('https://www.zztuku.com/user-signin.html', cookies=cookies, headers=headers)
    result = "".join(re.findall('''\"msg\":\"(.*?)\"''', response.text))
    return result


def get_score():
    response_text = requests.get('https://www.zztuku.com/user-logs.html', cookies=cookies, headers=headers).text
    page_text = response_text.replace('\/', '/').replace(r'\"', '''"''').strip('"')
    # print(page_text)
    # with open('space.html', 'w', encoding='utf-8')as f:
    #     f.write(page_text)
    tree = etree.HTML(page_text)
    score = "".join(tree.xpath('/html/body/header/div/div[4]/div/div[1]/p/text()')).strip('\xa0')
    return score


def task():
    qiandao_info = get_qiandao_info()
    print(qiandao_info)
    score = get_score()
    msg = f"站长图库\t许高翔\t{now}\t{qiandao_info}\t积分【{score}】\n"
    title = f'xgx站长图库-{qiandao_info},{score}'
    print(title, msg)
    send_msg(title, msg, '')
    with open("log.txt", 'a', encoding='utf-8')as f:
        f.write(msg)



if __name__ == '__main__':
    task()
