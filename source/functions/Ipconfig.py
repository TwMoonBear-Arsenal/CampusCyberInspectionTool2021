import os
class Showip:
    def ipconfig():
        print(os.system('cmd/ipconfig'))
Showip.ipconfig()