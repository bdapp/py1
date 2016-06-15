# -*- coding:utf-8 -*-

import urllib2
import re
import zipfile

class XIONGMAO:
    def __init__(self):
        self.url = 'http://panda.sj.91.com/Service/NovelPay.aspx?qt=1007&name=%e7%89%b9%e7%a7%8d%e5%85%b5%e7%8e%8b%e7%ba%b5%e6%a8%aa%e9%83%bd%e5%b8%82&bookid=3026307015&siteid=15&sign=showvip&restype=5&freetype=1&isfull=0&sourceid=501&pi=1&ps=481&show=binary&sessionid=4_41_PandaBookAndroid4801__weixin_720x1280_nzv1+Lq3q2U=&ver=41&mt=4'
        self.flag = 1

    def httpOpen(self, url):
        print url
        opener = urllib2.build_opener()
        opener.addheaders = [('User-Agent','Dalvik/1.6.0 (Linux; U; Android 4.1.1; Samsung Galaxy S3 - 4.1.1 - API 16 - 720x1280 Build/JRO03S)')]
        resp = opener.open(url)
        result = resp.read()
        # print result
        return result

    def downLoad(self, path):
        r = self.httpOpen(path)
        with open("a.zip", "wb") as code:
            code.write(r)

        zf = zipfile.ZipFile('a.zip', 'r')
        for n in zf.namelist():
            data = zf.read(n)
            with open('a.txt', 'ab+') as f:
                f.write(data)

                print '完成' + str(self.flag)
                self.flag+=1


    def start(self):
        result = self.httpOpen(self.url)
        p = re.compile('(极品老板娘_.*? )', re.S)
        r = re.findall(p, result)
        i = 1
        for t in r:
            s = t.strip()
            if s.find('zip') != -1:
                continue
            else:
                print s
                print i
                if (i<10):
                    f = 'http://res.sj.91.com/site-15(new)/30/3026307/000' +str(i)+ ' '+ s+ '.zip'
                    self.downLoad(f)
                if (10<=i<100):
                    f = 'http://res.sj.91.com/site-15(new)/30/3026307/00' + str(i) + ' ' + s + '.zip'
                    self.downLoad(f)
                if (100<=i<1000):
                    f = 'http://res.sj.91.com/site-15(new)/30/3026307/0' + str(i) + ' ' + s + '.zip'
                    self.downLoad(f)
                i+=1

xm = XIONGMAO()
xm.start()
