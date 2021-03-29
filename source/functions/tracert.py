import os
import platform

class traceip():
    def tracert(trace): 
        trace = input('請輸入目標ip或網域 : ')
        if platform.system() == 'Windows':
            return os.system('tracert '+trace)
        elif platform.system() == 'Linux':
            return os.system('traceroute '+trace)