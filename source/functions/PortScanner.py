import threading, multiprocessing
import sys
import socket
from datetime import datetime
class Scanport:
    @staticmethod
    def portscanner():
        #IP=raw_input('Input which u want to scan:').strip()
        target = socket.gethostbyname(raw_input('Input which u want to scan:').strip()) 
        
        # Add Banner 
        print("-" * 50)
        print("Scanning Target: " + target)
        print("Scanning started at:" + str(datetime.now()))
        print("-" * 50)
        try:
            # will scan ports between 1 to 65,535
            for port in range(1,65535):
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.setdefaulttimeout(0.0001)
                
                # returns an error indicator
                result = s.connect_ex((target,port))
                if result ==0:
                    print("Port {} is open".format(port))
                s.close()
        except KeyboardInterrupt:
                print("\n Exitting Program !!!!")
                sys.exit()
        except socket.gaierror:
                print("\n Hostname Could Not Be Resolved !!!!")
                sys.exit()
        except socket.error:
                print("\ Server not responding !!!!")
                sys.exit()
                print("Scanning stopped at:" + str(datetime.now()))
    @staticmethod
    def thread_job():
        for i in range(multiprocessing.cpu_count()):
                t = threading.Thread(target=Scanport.portscanner) 
        t.start()
#Scanport.thread_job()