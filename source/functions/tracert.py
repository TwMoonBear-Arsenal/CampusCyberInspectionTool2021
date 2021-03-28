import os
import platform

class traceip():
    def tracert(target):
        if platform.system() == 'Windows':
            return os.system('tracert '+target)
        elif platform.system() == 'Linux':
            return os.system('traceroute '+target)