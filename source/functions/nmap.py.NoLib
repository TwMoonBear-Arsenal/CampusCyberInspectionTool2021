from FuncBase import FuncBase
import os
import wget
import subprocess


def nmap():

    @property
    def Description(self):
        return('Nmap')

    def Run(self):
        IP = input("輸入ip:")
        nmap = "nmap " + IP
        subprocess = subprocess.Popen(nmap, shell=True, stdout=subprocess.PIPE)
        subprocess_return = subprocess.stdout.read()
        with open("result.txt", "wb") as file:
            file.write(subprocess_return)
        return
