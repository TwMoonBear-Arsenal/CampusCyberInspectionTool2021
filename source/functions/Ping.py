import os
#1100533005張庭維

class ping:
  def simpleping():
    hostname = input('請輸入目標：') 
    response = os.system("ping " + hostname)
    if response == 0:
      print(hostname , 'is up!')
    else:
      print(hostname , 'is down!')

class ping2:
  def hardping():
    hostname = input('請輸入目標：') 
    x = hostname.split(sep=".")
    uphost = set()
    for i in range(1,256):
        testhostname = x[0]+"."+x[1]+"."+x[2]+"."+str(i)
        response = os.system("ping -n 1 -w 1 " + testhostname)
        if response == 0:
          uphost.add(testhostname)
        os.system("cls")
    for i in uphost:
      print(i, end = ' is up.\n')


class ping3:
  def veryhardping():
    hostname = input('請輸入目標(格式example:192.168.136.0/24)：') 
    cidr = hostname.split(sep="/")
    number = 2 ** (32-int(cidr[1]))
    x = cidr[0].split(sep=".")
    uphost = set()
    for i in range(1,number):
      #加上去
      x[3] = str(int(x[3]) + 1)
      
      #判斷進位~~~
      if int(x[3]) + 1 == 256:
        x[3] = "0"
        x[2] = str(int(x[2]) + 1)
      if int(x[2]) + 1 == 256:
        x[2] = "0"
        x[1] = str(int(x[1]) + 1)
      if int(x[1]) + 1 == 256:
        x[1] = "0"
        x[0] = str(int(x[0]) + 1)

      #跑起來
      testhostname = x[0]+"."+x[1]+"."+x[2]+"."+x[3]
      response = os.system("ping -n 1 -w 1 " + testhostname)
      if response == 0:
        uphost.add(testhostname)
      os.system("cls")
    for i in uphost:
      print(i, end = ' is up.\n')