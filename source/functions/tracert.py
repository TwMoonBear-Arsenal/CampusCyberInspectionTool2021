import os
import platform

class traceip():
    def tracert():
        if platform.system() == 'Windows':
            return os.system('tracert '+input('請輸入目標ip或網域 : '))
        elif platform.system() == 'Linux':
            return os.system('traceroute '+input('請輸入目標ip或網域 : '))