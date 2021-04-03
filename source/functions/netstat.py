from FuncBase import FuncBase
import os


class Netstat():

    @property
    def Description(self):
        return('Netstat')

    def Run(self):
        return os.system('netstat -ano')
