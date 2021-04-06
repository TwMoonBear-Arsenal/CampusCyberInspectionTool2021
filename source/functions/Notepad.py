import os


class Notepad():

    @property
    def Description(self):
        return('NotePad')

    def Run(self):
        i = 10
        while(i > 0):
            os.system("start notepad")
            i = i-1
