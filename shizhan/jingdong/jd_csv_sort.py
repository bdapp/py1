# -*- coding:utf-8 -*-
'''
对csv文件里面的数据进行提取、排序、合并计算总评价数
'''
import csv
import re
import os

class ADD:

    def __init__(self, file):
        self.file_name = file


    # 处理系统版本字段
    def get_system_version(self, version):
        try:
            p = re.compile('(\w*\s(\d|\w\d)(\.\d*|\d*))', re.S)
            v = re.search(p, version)
            print ';; ' + version
            print v.group(1).strip()
            return v.group(1).strip()
        except Exception:
            print '获取系统版本异常'
            print ''


    def get_csv_list(self):
        try:
            # 打开并处理csv文件
            with open(self.file_name, 'rb') as f:
                rows = csv.reader(f, delimiter=',', quotechar='|')

                ll = []
                for r in rows:
                    # 把内容写入到list
                    if r[len(r) - 1] != '评价':
                        ver = self.get_system_version(r[6])
                        if ver is None or ver == '':
                            ver = ''
                        ll.append((r[1].upper(), int(r[len(r) - 1]), ver))
                print len(ll)

                return ll

        except Exception:
            print '对csv文件的排序、计算异常'
            return []


    def get_hots(self):
        ll = self.get_csv_list()
        # 对list的第一次排序(产品型号)
        ll.sort(lambda x, y: cmp(x[0], y[0]))
        print ll
        # 对排序好的list的评价进行合并试算
        n = ''
        v = 0
        ln = []
        for i in ll:
            # 型号不为空并且和上一条记录相同的，评价值相加
            if i[0] != '' and i[0] == n:
                v = v + i[1]
                continue
            else:
                ln.append((n, v))
                n = i[0]
                v = i[1]

        print len(ln)

        # 对相加生成的新list进行按评价多少排序
        ln.sort(lambda x, y: cmp(x[1], y[1]))
        # 对排序完的新list进行反转（变成从大到小）
        ln.reverse()

        return ln


    def get_version(self):
        ll = self.get_csv_list()
        # 对list的第一次排序(系统版本)
        ll.sort(lambda x, y: cmp(x[2], y[2]))
        print ll
        # 对排序好的list的评价进行合并试算
        c = ''
        v = 0
        ln = []
        for i in ll:
            # 型号不为空并且和上一条记录相同的，评价值相加
            if i[2] != '' and i[2] == c:
                v = v + i[1]
                continue
            else:
                if c!='':
                    ln.append((c, v))
                c = i[2]
                v = i[1]

        print len(ln)

        # 对相加生成的新list进行按评价多少排序
        ln.sort(lambda x, y: cmp(x[1], y[1]))
        # 对排序完的新list进行反转（变成从大到小）
        ln.reverse()
        print ln
        return ln

