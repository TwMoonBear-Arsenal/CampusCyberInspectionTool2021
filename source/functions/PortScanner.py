import socket  
class Option:
    
    # 建構式
    def __init__(self, number, descritpion):
        self.number = number  # 編號
        self.descritpion = descritpion  # 說明文字
class Scanport:
    def portscannerTCP():
        ip = input('\033[0;31;42mInput IP which you want to know open ports:\n\033[0m').strip()  #getting ip-address of host
        for port in range(65535):      #check for all available ports
            try:
                serv = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # create a new socket
                serv.bind((ip,port)) # bind socket with address  
            except:
                print('\033[32m[OPEN]\033[0m Port open :',port) #print open port number
            serv.close() #close connection
    def portscannerUDP():
        ip = input('\033[0;31;42mInput IP which you want to know open ports:\n\033[0m').strip()  #getting ip-address of host
        for port in range(65535):      #check for all available ports
            try:
                serv = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # create a new socket
                serv.bind((ip,port)) # bind socket with address  
            except:
                print('\033[32m[OPEN]\033[0m Port open :',port) #print open port number
            serv.close() #close connection
class Portscanneroption:
    def option():
        optionList = []
        optionList.append(Option(1, "TCP"))
        optionList.append(Option(2, "UDP"))
        for option in optionList:
            print("[", option.number, "] ", option.descritpion)
        selection = input("請輸入需要的功能：").strip()
        if(selection=="1"):
            Scanport.portscannerTCP()
        elif(selection=="2"):
            Scanport.portscannerUDP()
#Scanport.portscanner()
#Portscanneroption.option()