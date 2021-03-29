import os
import wget
def nmap():
    try:    
        IP=input("輸入ip or domain name:")
        nmap="nmap "+IP
        print(nmap)
        os.system( nmap )
    except():
        file=wget.download('https://nmap.org/dist/nmap-7.91-setup.exe')
        return nmap()