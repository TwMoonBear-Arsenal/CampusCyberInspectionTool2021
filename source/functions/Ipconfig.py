import socket
class Showip:
    def ipconfig():
        myname = socket.getfqdn(socket.gethostname())
        get_s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        get_s.connect(('8.8.8.8', 0))
        ip = ('hostname: %s, localIP: %s') % (myname, get_s.getsockname()[0])
        print(ip)
        return ip
#Showip.ipconfig()