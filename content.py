#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'LENOVO'
import hashlib
import urllib.request
import json
import random
def query_content(q):
    appid = '20190314000277133'
    secretKey = 'BoLJPqcbnwXTGJJvy_Nc'
    httpClient = None
    myurl = 'http://api.fanyi.baidu.com/api/trans/vip/translate'
    fromLang = 'auto'
    toLang = 'auto'
    salt = random.randint(32768, 65536)
    sign = appid + q + str(salt) + secretKey
    m1 = hashlib.md5()
    m1.update(sign.encode(encoding='utf-8'))
    sign = m1.hexdigest()
    myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(
        q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(salt) + '&sign=' + sign
    response = urllib.request.urlopen(myurl).read().decode('utf8')
    getJson = json.loads(response)
    getInfo = getJson['trans_result']
    s = getInfo[0]
    re = s['dst']
    return re
