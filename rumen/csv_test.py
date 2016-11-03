# -*- coding:utf-8 -*-
'''
对CSV文件的读取、写入
author: Bello
'''

import csv
import sys
reload(sys)
sys.setdefaultencoding('utf8')


# 写入
with open('/home/ubt/mm.csv', 'wb') as f:
    w = csv.writer(f, dialect='excel')
    w.writerow(['a','1','2','3','4','哈'.encode('gb2312')])
    w.writerow(['b','22','44','55','66',])

# 读取
with open('/home/ubt/mobile.csv', 'rb') as f:
    rr = csv.reader(f, delimiter=' ', quotechar='|')
    for row in rr:
        print '\n'
        print row

