import hashlib
# 导入time模块
import time
import requests
import json


def Md5(res):
    print(res)
    md = hashlib.md5()  # 构造一个md5
    md.update(res.encode(encoding='utf-8'))
    # 加密
    print(md.hexdigest().upper())
    return md.hexdigest().upper()


def testapi():
    tures = {}
    restime = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    # restime="20190829114035"
    # 传入参数
    tures['timestamp'] = restime
    tures['app_id'] = "a4a5afd0b1994048"
    tures['version'] = '1.0'
    tures['method'] = 'jiuti'
    tures['imgpath'] = 'https://bys-tonguepicture.oss-cn-beijing.aliyuncs.com/1563412989396.jpg'
    tures['sign'] = Md5(Md5(restime) + "0a2a94839f9c4d48a88cb74c2cdf335e")
    url = "http://www.bayescience.com/api/analysis"
    response = requests.post(url, params=tures)
    # print(response.text)
    print(type(response.text))
    load = json.loads(response.text)
    print(load)
testapi()
