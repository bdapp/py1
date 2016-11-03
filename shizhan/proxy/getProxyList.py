# -*- coding:utf-8 -*-

import urllib2
import re
import time


class PROXY:
    def __init__(self):
        # 国内普通
        # self.url = 'http://proxy.mimvp.com/free.php?proxy=in_tp'
        # 国内高匿
        self.url = 'http://proxy.mimvp.com/free.php?proxy=in_hp'
        # 国外普通
        # self.url = 'http://proxy.mimvp.com/free.php?proxy=out_tp'
        # 国外高匿
        # self.url = 'http://proxy.mimvp.com/free.php?proxy=out_hp'

        self.fileName = './proxy.txt'

    def getProxy(self):
        # 走代理
        enable_proxy = False
        proxy_handler = urllib2.ProxyHandler({'http':'116.54.123.48:8888'})
        null_proxy_handler = urllib2.ProxyHandler({})
        if enable_proxy:
            opener = urllib2.build_opener(proxy_handler)
        else:
            opener = urllib2.build_opener(null_proxy_handler)
        urllib2.install_opener(opener)

        response = opener.open(self.url)
        result = response.read()
        # print result

        pattern = re.compile("<td style='text-align: center; color:blue;'>(.*?)<.*?<td>(.*?)</td.*?<img src=(.*?)/>.*?;overflow:hidden;' title='(.*?)'.*?<td title='(.*?)秒'", re.S)
        items = re.findall(pattern, result)

        with open(self.fileName, 'ab') as f:
            localTime = time.asctime(time.localtime(time.time()))
            f.write('\n\n================== '+ localTime +' ==================\n\n')

        ipList = []

        for x in items:
            p = 'null'
            if x[2].find('yvMpwO0OO0O') != -1:
                p = '23'
            elif x[2].find('MpAO0OO0O') != -1:
                p = '80'
            elif x[2].find('QO0OO0O') != -1:
                p = '81'
            elif x[2].find('gO0OO0O') != -1:
                p = '82'
            elif x[2].find('4vMpwO0OO0O') != -1:
                p = '83'
            elif x[2].find('0vNpDMO0O') != -1:
                p = '443'
            elif x[2].find('4vNpDMO0O') != -1:
                p = '843'
            elif x[2].find('4vMpDgO0O') != -1:
                p = '808'
            elif x[2].find('NpAO0OO0O') != -1:
                p = '84'
            elif x[2].find('mzvMpTI4') != -1:
                p = '3128'
            elif x[2].find('m2vNpjY2') != -1:
                p = '6666'
            elif x[2].find('4vMpDAw') != -1:
                p = '8000'
            elif x[2].find('m4vMpDAz') != -1:
                p = '8003'
            elif x[2].find('m4vMpDgw') != -1:
                p = '8080'
            elif x[2].find('pDgx') != -1:
                p = '8081'
            elif x[2].find('MpDg4') != -1:
                p = '8088'
            elif x[2].find('MpDkw') != -1:
                p = '8090'
            elif x[2].find('pTAx') != -1:
                p = '8101'
            elif x[2].find('pTE4') != -1:
                p = '8118'
            elif x[2].find('4vOpDg4') != -1:
                p = '8888'
            elif x[2].find('5vMpDAw') != -1:
                p = '9000'
            elif x[2].find('5vNpzk3') != -1:
                p = '9797'
            elif x[2].find('5vOpTk5') != -1:
                p = '9999'
            elif x[2].find('xvMpDAwMAO0OO0O') != -1:
                p = '10000'
            elif x[2].find('pDIwMAO0OO0O') != -1:
                p = '10200'
            elif x[2].find('yvMpDAwMAO0OO0O') != -1:
                p = '20000'
            elif x[2].find('zvOpTkwMAO0OO0O') != -1:
                p = '39900'
            elif x[2].find('pzAwMAO0OO0O') != -1:
                p = '63000'

            if x[4].find('999') == -1:
                with open(self.fileName, 'ab') as f:
                    f.writelines(x[0] + '\t' + x[1] + '\t' + p + '\t' + x[3] + '\t' + x[4] + '\n')
                    if p != 'null':
                        if x[3].find('/')!=-1:
                            h = x[3].split('/')
                            ipList.append(h[0].lower() + '://'+x[1]+':' + p)
                            ipList.append(h[1].lower() + '://'+x[1]+':' + p)
                        else:
                            ipList.append(x[3].lower()+ '://' + x[1] + ':' + p)

        print ipList
        print '写入完成'
        return ipList

#proxy = PROXY()
#proxy.getProxy()