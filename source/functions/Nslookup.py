import socket

class Nslookup:
    def domainip():
        a = input('\033[32mInpput you need to search hostname:\033[0m\n').strip()
        print(f'The \033[34m{a}\033[0m IP Address is \033[31m{socket.gethostbyname(a)}\033[0m')
    def ipdomain():
        a = input('\033[32mInpput you need to search IP:\033[0m\n').strip()
        print(f'The \033[34m{a}\033[0m Hostname is \033[31m{socket.gethostbyaddr(a)}\033[0m')
#Nslookup.dnsip()
#Nslookup.ipdomain()
