import socket  
class Scanport:
    def portscanner():
        ip = input('\033[0;31;42mInput IP which you want to know open ports:\n\033[0m').strip()  #getting ip-address of host
        for port in range(65535):      #check for all available ports
            try:
                serv = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # create a new socket
                serv.bind((ip,port)) # bind socket with address  
            except:
                print('\033[32m[OPEN]\033[0m Port open :',port) #print open port number
            serv.close() #close connection
#Scanport.portscanner()