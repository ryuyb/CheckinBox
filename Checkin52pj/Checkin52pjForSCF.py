# -*- coding: utf8 -*-

import requests, os, sys
sys.path.append('.')
requests.packages.urllib3.disable_warnings()
try:
    from pusher import pusher
except:
    pass
from bs4 import BeautifulSoup

cookie = os.environ.get('cookie_52pj')

def main(*args):
    try:
        msg = ""
        s = requests.Session()
        headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
            'Cookie': cookie,
            'ContentType':'text/html;charset=gbk'
        }
        s.get('https://www.52pojie.cn/home.php?mod=task&do=apply&id=2', headers=headers)
        a = s.get('https://www.52pojie.cn/home.php?mod=task&do=draw&id=2', headers=headers)
        b = BeautifulSoup(a.text,'html.parser')
        c = b.find('div',id='messagetext').find('p').text

        if "您需要先登录才能继续本操作"  in c:
            pusher("52pojie  Cookie过期", c)
            print("cookie_52pj失效，需重新获取")
            msg += "cookie_52pj失效，需重新获取"
        elif "恭喜"  in c:
            print("52pj签到成功")
            msg += "52pj签到成功"
        else:
            print(c)
    except:
        print("52pj出错,大概率是触发52pj安全防护，访问出错。自行修改脚本运行时间和次数，总有能访问到的时间")
        msg += "52pj出错,大概率是触发52pj安全防护，访问出错。自行修改脚本运行时间和次数，总有能访问到的时间"
        print("如果错误需要推送的话，自行去掉代码内的注释")
        #pusher("52pojie  签到失败", b)
    return msg + "\n"

def pjCheckin(*args):
    msg = ""
    global cookie
    if "\\n" in cookie:
        clist = cookie.split("\\n")
    else:
        clist = cookie.split("\n")
    i = 0
    while i < len(clist):
        msg += f"第 {i+1} 个账号开始执行任务\n"
        cookie = clist[i]
        msg += main(cookie)
        i += 1
    return msg

if __name__ == "__main__":
    if cookie:
        print("----------52pojie开始尝试签到----------")
        pjCheckin()
        print("----------52pojie签到执行完毕----------")
