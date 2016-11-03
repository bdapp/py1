# -*- coding:utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import random

people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
y_pos = np.arange(len(people))

value = [10, 12,16,19,20]

# 获取随机颜色值
colors = []
for v in value:
    c='#'
    for i in random.sample([1,2,3,4,5,6,7,8,9,0,'a','b','c','d','e','f'], 6):
        c = c+str(i)
    colors.append(c)

print colors



plt.bar(y_pos, value, width=0.7, align='center', color=colors, alpha=0.3)
plt.xticks(y_pos, people)
plt.ylim(ymax=30, ymin=0)
plt.xlabel('Performance')
plt.title('How fast do you want to go today?')

plt.show()