from os import name
import sys


class Path:

    @property
    def Description(self):
        return('顯示Python環境路徑')

    def Run(self):
        print(sys.path)
        return
