import os

hostname = input('請輸入目標：') #example
response = os.system("ping " + hostname)

#and then check the response...
if response == 0:
  print(hostname , 'is up!')
else:
  print(hostname , 'is down!')