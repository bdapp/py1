# -*- coding:utf-8 -*-

import time
import matplotlib.pyplot as plt
import numpy as np

def get_memory():
    return 100*(0.5+0.5*np.sin(0.5*np.pi*time.time()))

def get_cpu():
    return 100*(0.5 +0.5*np.sin(0.2*np.pi*(time.time()-0.25)))

def get_net():
    return 100*(0.5+0.5*np.sin(0.7*np.pi*(time.time() - 0.1)))

def get_status():
    return get_memory(), get_cpu(), get_net()

fig, ax = plt.subplots()
ind = np.arange(1, 4)

plt.show(block=False)

pm, pc, pn = plt.bar(ind, get_status())
centers = ind + 0.5*pm.get_width()
pm.set_facecolor('r')
pc.set_facecolor('g')
pn.set_facecolor('b')
ax.set_xlim(0.5, 4)
ax.set_xticks(centers)
ax.set_ylim(0, 100)
ax.set_xticklabels(['Memory', 'CPU', 'Bandwidth'])
ax.set_ylabel('Percent usage')
ax.set_title('System Monitor')

start = time.time()
for i in range(200):
    m, c, n = get_status()

    pm.set_height(m)
    pc.set_height(c)
    pn.set_height(n)

    fig.canvas.draw_idle()
    try:
        fig.canvas.flush_events()
    except NotImplementedError:
        pass


stop = time.time()
print stop - start
