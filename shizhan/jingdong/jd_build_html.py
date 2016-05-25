# -*- coding:utf-8 -*-
'''
根据统计结果生成统计图页面
'''

import json
import webbrowser
import os
import jd_csv_sort


class RESULT:

    def __init__(self):
        self.js = './html/data.js'     # 数据文件
        self.html = './html/py.html'   # 结果展示页
        self.ph = 10                   # 排行榜数量

        self.num = 0   # 品牌数量
        self.type = [] # 品牌名称
        self.pro = []   # 型号+评价
        self.sys = []   # 系统+评价
        self.vers = []  # 系统版本

    # 生成data文件
    def write_file(self):
        try:
            with open(self.js, 'ab') as f:
                f.write('var num=' + str(self.num) + '\n')
                f.write('var type=' + json.dumps(self.type) + '\n')
                f.write('var pro=' + json.dumps(self.pro) + '\n')
                f.write('var sys=' + json.dumps(self.sys) + '\n')
                f.write('var vers=' + json.dumps(self.vers) + '\n')

        except Exception:
            print '写入data.js文件出错'

    # 从csv文件获取数据
    def build_html(self, file):

            add = jd_csv_sort.ADD('./file/' + file)
            # 获取热门排行数据
            rs = add.get_hots()
            # 获取系统排行数据
            system_line = add.get_version()

            # 热门数据分别写到两个list
            data = []
            categories = []
            # 系统排行写入两个list
            version = []
            ver_name = []

            try:
                for r in range(0, self.ph):
                    print rs[r][1]
                    print rs[r][0]
                    data.append(rs[r][1])
                    categories.append(rs[r][0])

            except Exception as e:
                print e

            try:
                for i in range(0, len(system_line)):
                    mdic = {}
                    mdic['name'] = system_line[i][0]
                    mdic['value'] = system_line[i][1]
                    version.append(mdic)
                    ver_name.append(system_line[i][0])
            except Exception as e:
                print e


            # 写入json
            pro_list = {}
            pro_list["categories"] = categories
            pro_list["data"] = data
            self.pro.append(pro_list)

            self.sys.append(version)
            self.vers.append(ver_name)


    def start(self):
        l = os.listdir('./file/')
        self.num = len(l)
        for i in l:
            print i
            self.type.append(i.replace('.csv', ''))
            self.build_html(i)

        self.write_file()

        # 打开浏览器
        webbrowser.open(self.html)


result = RESULT()
result.start()