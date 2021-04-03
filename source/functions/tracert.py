from FuncBase import FuncBase
import os
import platform


class Traceip(FuncBase):

    @property
    def Description(self):
        return('Tracert')

    def Run(self):
        if platform.system() == 'Windows':
            return os.system('tracert '+input('請輸入目標ip或網域 : '))
        elif platform.system() == 'Linux':
            return os.system('traceroute '+input('請輸入目標ip或網域 : '))
