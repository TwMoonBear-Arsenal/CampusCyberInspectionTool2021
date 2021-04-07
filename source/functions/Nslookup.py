import socket

class Option:
    
    # 建構式
    def __init__(self, number, descritpion):
        self.number = number  # 編號
        self.descritpion = descritpion  # 說明文字
class Nslookup:
    def domainip():
        a = input('\033[32mInpput you need to search hostname:\033[0m\n').strip()
        print(f'The \033[34m{a}\033[0m IP Address is \033[31m{socket.gethostbyname(a)}\033[0m')
    def ipdomain():
        a = input('\033[32mInpput you need to search IP:\033[0m\n').strip()
        print(f'The \033[34m{a}\033[0m Hostname is \033[31m{socket.gethostbyaddr(a)}\033[0m')
class Nslookupoption:
    def option():
        optionList = []
        optionList.append(Option(1, "hostname2ip"))
        optionList.append(Option(2, "ip2hostname"))
        for option in optionList:
            print("[", option.number, "] ", option.descritpion)
        selection = input("請輸入需要的功能：").strip()
        if(selection=="1"):
            Nslookup.domainip()
        elif(selection=="2"):
            Nslookup.ipdomain()
#Nslookup.dnsip()
#Nslookup.ipdomain()
#Nslookupoption.option()