# -*- coding:utf-8 -*-

import csv

with open('/home/ubt/mo.csv', 'rb') as f:
    rows = csv.reader(f, delimiter=',', quotechar='|')
    '''
    rows2 = rows
    for r in rows:
        print r
        pro_name = r[1]
        price = r[len(r)-1]
        print pro_name
        print price

        if pro_name != '型号' and pro_name!='':
            for r2 in rows2:
                pro_name2 = r2[1]
                price2 = r2[len(r2)-1]
                #if pro_name.lower() == pro_name2.lower():
                    #price = int(price) + int(price2)
                    #print price
            print pro_name
            print price
    '''


