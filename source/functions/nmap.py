import os
import wget
import subprocess
#file=wget.download('https://nmap.org/dist/nmap-7.91-setup.exe')

IP=input("輸入ip:")
nmap= "nmap " + IP  
#os.system( nmap ) 

subprocess = subprocess.Popen(nmap, shell=True, stdout=subprocess.PIPE)
subprocess_return = subprocess.stdout.read()

with open("result.txt", "wb") as file:
    file.write(subprocess_return)

