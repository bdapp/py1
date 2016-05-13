# -*- coding:utf-8 -*-

import urllib2
import re
import time

# 国内普通
#url = 'http://proxy.mimvp.com/free.php?proxy=in_tp'
# 国内高匿
url = 'http://proxy.mimvp.com/free.php?proxy=in_hp'
# 国外普通
#url = 'http://proxy.mimvp.com/free.php?proxy=out_tp'
# 国外高匿
#url = 'http://proxy.mimvp.com/free.php?proxy=out_hp'

fileName = './proxy.txt'

# 走代理
enable_proxy = True
proxy_handler = urllib2.ProxyHandler({'http':'http://123.56.28.196:8888'})
null_proxy_handler = urllib2.ProxyHandler({})
if enable_proxy:
    opener = urllib2.build_opener(proxy_handler)
else:
    opener = urllib2.build_opener(null_proxy_handler)
urllib2.install_opener(opener)

response = opener.open(url)
result = response.read()

pattern = re.compile("<td style='text-align: center; color:blue;'>(.*?)<.*?<td>(.*?)</td.*?<img src=(.*?)/>.*?<td title='(.*?)秒'", re.S)
items = re.findall(pattern, result)

with open(fileName, 'ab') as f:
    localTime = time.asctime(time.localtime(time.time()))
    f.write('\n\n================== '+ localTime +' ==================\n\n')

for x in items:
    p = 'null'
    if x[2].find('MpAO0OO0O') != -1:
        p = '80'
    if x[2].find('QO0OO0O') != -1:
        p = '81'
    if x[2].find('gO0OO0O') != -1:
        p = '82'
    if x[2].find('wO0OO0O') != -1:
        p = '83'
    if x[2].find('pDMO0O') != -1:
        p = '808'
    if x[2].find('pDgO0O') != -1:
        p = '808'
    if x[2].find('NpAO0OO0O') != -1:
        p = '84'
    if x[2].find('pTI4') != -1:
        p = '3128'
    if x[2].find('pjY2') != -1:
        p = '6666'
    if x[2].find('4vMpDAw') != -1:
        p = '8000'
    if x[2].find('pDAz') != -1:
        p = '8003'
    if x[2].find('pDgw') != -1:
        p = '8080'
    if x[2].find('pDgx') != -1:
        p = '8081'
    if x[2].find('MpDg4') != -1:
        p = '8088'
    if x[2].find('pTAx') != -1:
        p = '8101'
    if x[2].find('OpDg4') != -1:
        p = '8888'
    if x[2].find('5vMpDAw') != -1:
        p = '9000'
    if x[2].find('pzk3') != -1:
        p = '9797'
    if x[2].find('pTk5') != -1:
        p = '9999'
    if x[2].find('pDIwMAO0OO0O') != -1:
        p = '10200'
    if x[2].find('pTkwMAO0OO0O') != -1:
        p = '39900'

    if x[3].find('999') == -1:
        with open(fileName, 'ab') as f:
            f.writelines(x[0] + '\t' + x[1] + '\t' + p + '\t' + x[3] + '\n')

print '写入完成'