import time
from urllib import request

import re
import os


def getReq(url):  # 读取网页源码
    url_req = request.urlopen(url)
    data = url_req.read().decode('UTF-8')  # 将数据解析为：UTF-8格式
    return data


def gethtml(data):  # 选择需要爬取的标签
    tr = re.findall(r'<li><a (.*)</a></li>', data, re.S)

    firsttable = tr[0]

    htmllist = re.findall(r'href="(.*?)</a></li>', firsttable)  # 二次筛选

    return htmllist


try:
    ip_addr = input("请输入需要爬取的URL:")
    data = getReq(ip_addr)
    htmllist = gethtml(data)
    local = os.getcwd()
    scanner_file = local + "\网站爬取目录.txt"
    file_save = open(scanner_file, 'w')  # 保存目录
    for h1 in htmllist:
        newurl = ip_addr + h1
        firsttable = newurl.replace('">', ' ')
        print(firsttable)
        file_save.write(firsttable + '\n')
    file_save.close()
except:
    print("参数错误/网络存在问题")
print()
print("爬取的目录已保存到：网站爬取目录.txt 文件中")
time.sleep(200)
