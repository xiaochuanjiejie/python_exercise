__author__ = 'chuan'

import psutil

mem = psutil.virtual_memory()
cpu1 = psutil.cpu_times()
cpu2 = psutil.cpu_times(percpu=True)
print cpu1
print cpu2