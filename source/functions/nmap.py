import os
import wget
import subprocess
def nmap():
    
    IP=input("輸入ip:")
    nmap= "nmap " + IP  
    subprocess = subprocess.Popen(nmap, shell=True, stdout=subprocess.PIPE)
    subprocess_return = subprocess.stdout.read()
    with open("result.txt", "wb") as file:
        file.write(subprocess_return)

