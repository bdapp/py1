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
        self.html = './html/index.html'   # 结果展示页
        self.num = 10                   # 排行榜数量

    def build_html(self, file):
        add = jd_csv_sort.ADD('./file/' + file)
        # 获取热门排行数据
        rs = add.get_hots()
        # 获取系统排行数据
        system_line = add.get_version()


        # 热门数据分别写到两个list
        value = []
        pro = []
        for r in range(0, self.num):
            value.append(rs[r][1])
            pro.append(rs[r][0])

        # 写入json
        data = {}
        data["categories"] = pro
        data["data"] = value
        j = json.dumps(data)
        print j

        # 系统排行写入两个list
        version = []
        ver_name = []
        print system_line
        for i in range(0, len(system_line)):
            mdic = {}
            mdic['name'] = system_line[i][0]
            mdic['value'] = system_line[i][1]
            version.append(mdic)
            ver_name.append(system_line[i][0])

        # 写入json
        v_json = json.dumps(version)
        n_json = json.dumps(ver_name)
        print v_json, n_json


        # json写入数据文件
        with open(self.js, 'ab') as f:
            file = file.replace('.csv', '_')
            co = 'var '+file+'c=' + j
            vo = 'var '+file+'v=' + v_json
            vn = 'var '+file+'v_n=' + n_json
            f.write(co)
            f.write('\n')
            f.write(vo)
            f.write('\n')
            f.write(vn)
            f.write('\n')


        # 生成html
        with open(self.html, 'wb') as f:
            f.write('<!DOCTYPE html> \n')
            f.write('<html> \n')
            f.write('<head> \n')
            f.write('    <meta charset="utf-8"> \n')
            f.write('    <!-- 引入 ECharts 文件 --> \n')
            f.write('    <script src="./echarts.min.js"></script> \n')
            f.write('    <script type="text/javascript" src="./jquery.min.js"></script> \n')
            f.write('    <script type="text/javascript" src="./jquery.min.js"></script> \n')


        # 打开浏览器
        webbrowser.open(self.html)

    def start(self):
        l = os.listdir('./file/')
        for i in l:
            print i
            self.build_html(i)

result = RESULT()
result.start()