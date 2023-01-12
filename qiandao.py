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
    'PHPSESSID': 'r225k1spluvamdcfi87u963el0',
    'Hm_lvt_36d091ca4167858e40c7bf39f954e3f9': '1672189552',
    '__bid_n': '1855643a829e3f11034207',
    'FEID': 'v10-7a0fd5d6246e8a62cc7ab21039dc6c1f31172b31',
    '__xaf_fpstarttimer__': '1672189552797',
    'FPTOKEN': 'LRolPOSmrn/r1FsAXT/Adc5GAJCS922XIwtvrKXYZ1lLuMExo2qZYUBWO9oIJ1KlzBQ7yzxwFoIPnRSZGjjH6NfsSq3CvPK3l9pJDyPks5ranwpE3hMO4wrzyY6b4iDMVFKOOs18pDdYZ5nQGOpiqHRmLKBstJ+WIEkre9olFSJFL48Mcv2j/y+iV1RhrtxL//PurIVK/IGyZ7jk6XPmDSuXg++fmSIhjU7sad6S4Kp2DGS/bDqkztswWusX8ekBX1Jgu3aiTFCh20Dikd5qsPbAkOZWVZ+BzzHlGDKV0vE/i1iGASqh/wGL4pKWV9nZdaNJRArlu7UZ9t0e8g45K8ZY8o67DiMb2chyPvqQO05LjEMPTRWKG1djSBrXS+HRikjQN+UlwS14aaJhjQmmazPblqsZcDP1ApxgVWPNYcnOSSKk9oN2IFNo/D/QLrCs|NyRavl/iUvb5FG9wEyCB1o8Ys8wTcb/yq26d0DMSJdY=|10|8cb073f32b7dc490c0750deb0b7bcfaf',
    '__xaf_fptokentimer__': '1672189553109',
    '__xaf_ths__': '{"data":{"0":1,"1":43200,"2":60},"id":"afa4b091-db58-40de-bf67-b05caab20768"}',
    '__xaf_thstime__': '1672189553112',
    'BAIDU_SSP_lcr': 'https://graph.qq.com/',
    'Hm_lpvt_36d091ca4167858e40c7bf39f954e3f9': '1672191052',
}

headers = {
    'authority': 'www.zztuku.com',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    # 'content-length': '0',
    # 'cookie': 'PHPSESSID=r225k1spluvamdcfi87u963el0; Hm_lvt_36d091ca4167858e40c7bf39f954e3f9=1672189552; __bid_n=1855643a829e3f11034207; FEID=v10-7a0fd5d6246e8a62cc7ab21039dc6c1f31172b31; __xaf_fpstarttimer__=1672189552797; FPTOKEN=LRolPOSmrn/r1FsAXT/Adc5GAJCS922XIwtvrKXYZ1lLuMExo2qZYUBWO9oIJ1KlzBQ7yzxwFoIPnRSZGjjH6NfsSq3CvPK3l9pJDyPks5ranwpE3hMO4wrzyY6b4iDMVFKOOs18pDdYZ5nQGOpiqHRmLKBstJ+WIEkre9olFSJFL48Mcv2j/y+iV1RhrtxL//PurIVK/IGyZ7jk6XPmDSuXg++fmSIhjU7sad6S4Kp2DGS/bDqkztswWusX8ekBX1Jgu3aiTFCh20Dikd5qsPbAkOZWVZ+BzzHlGDKV0vE/i1iGASqh/wGL4pKWV9nZdaNJRArlu7UZ9t0e8g45K8ZY8o67DiMb2chyPvqQO05LjEMPTRWKG1djSBrXS+HRikjQN+UlwS14aaJhjQmmazPblqsZcDP1ApxgVWPNYcnOSSKk9oN2IFNo/D/QLrCs|NyRavl/iUvb5FG9wEyCB1o8Ys8wTcb/yq26d0DMSJdY=|10|8cb073f32b7dc490c0750deb0b7bcfaf; __xaf_fptokentimer__=1672189553109; __xaf_ths__={"data":{"0":1,"1":43200,"2":60},"id":"afa4b091-db58-40de-bf67-b05caab20768"}; __xaf_thstime__=1672189553112; BAIDU_SSP_lcr=https://graph.qq.com/; Hm_lpvt_36d091ca4167858e40c7bf39f954e3f9=1672191052',
    'origin': 'https://www.zztuku.com',
    'pragma': 'no-cache',
    'referer': 'https://www.zztuku.com/',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
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
    msg = f"站长图库\t张杰\t{now}\t{qiandao_info}\t积分【{score}】\n"
    title = f'zj站长图库-{qiandao_info},{score}'
    print(title, msg)
    send_msg(title, msg, '')
    with open("log.txt", 'a', encoding='utf-8')as f:
        f.write(msg)



if __name__ == '__main__':
    task()
