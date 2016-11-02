# -*- coding:utf-8 -*-

# 利用cookie登录系统获取标题

import urllib
import urllib2
import re
import cookielib

class NOTE:
    def __init__(self):
        # 登录页面
        self.loginUrl = 'http://note.budor.cn:88/a?action=Login'
        # Tips页面
        self.tipsUrl = 'http://note.budor.cn:88/a?action=Tips'

        self.cookies = cookielib.CookieJar()
        self.postData = urllib.urlencode({
            'username':'bell4o',
            'password':'eagl4',
            'phonenumber':'15944'
        })
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookies))

    # 获取页面
    def getPage(self):
        request = urllib2.Request(
            url = self.loginUrl,
            data = self.postData
        )

        self.opener.open(request)
        result = self.opener.open(self.tipsUrl)
        return result.read()

    # 获取标题
    def getTitles(self):
        page = self.getPage()
        pattern = re.compile('<tr>.*?<td>.*?<td>(.*?)</td>', re.S)
        items = re.findall(pattern, page)
        for item in items:
            print item

note = NOTE()
note.getTitles()
