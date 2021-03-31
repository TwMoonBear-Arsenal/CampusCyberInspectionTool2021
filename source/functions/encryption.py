
import os
class cryto:

    def decryp_Vige() :
        cyphertext=input("cyphertext=")
        key=input("key=")

        print("plaintext=",end='')
        j=0
        for i in cyphertext :
            c=ord(key[j])
            if c < 97 :
                c=c+32
            c=c-97
            x=ord(i)+26
            if x < 123 :
                x=x-c
                if x > 90 :
                     x=x-26
            else :
                x=x-c
                if x > 122 :
                    x=x-26
            print(chr(x),end='') 
            j=j+1
        print("\n")
    
    def encryp_Vige() :
        plaintext=input("plaintext=")
        key=input("key=")
        print()
        print("cyphertext=",end='')
        j=0
        for i in plaintext :
            c=ord(key[j])
            if c < 97 :
                c=c+32
            c=c-97
            x=ord(i)-26
            if x < 65 :
                x=x+c
                if x < 65 :
                    x=x+26
            else :
                x=x+c    
                if x < 97 :
                    x=x+26
            print(chr(x),end='') 
            j=j+1
        print("\n")

    def Make_a_rsa() :
        print("公鑰(n,e) 只能加密小於n的整数m!!!")
        while(1) :
            p,q=map(int,input("choose two Prime number :(split with space)").split())
            if   p > 1 :  
                t=0
                for   i   in   range ( 2 , p ) : 
                    if   ( p % i ) == 0 : 
                        print ( "請輸入質數",end="")
                        t=1
                        break
                if t == 1 :
                    continue    
            if   q > 1 :
                t=0
                for   i   in   range ( 2 , q ) : 
                    if   ( q % i ) == 0 : 
                        print ( "請輸入質數",end="")
                        t=1
                    break
                if t == 1 :
                    continue
            break   
        n=p*q
        r=(p-1)*(q-1)
        e=0
        d=0
        for   i   in   range ( 2 , r ) : 
            if   ( r-int(r/i)*i ) == 1 :
                e=i
                break
        for   i   in   range ( 2 , r ) : 
            if   ( (i*e) % r ) == 1 :
                d=i
                break
        print("Public key(N,e)=({0},{1})\nPrivate key(N,d)=({2},{3})".format(n, e, n, d))

    def rsa_send() :
        import math
        import array as arr
        n,k=map(int,input("input your key :(split with space)").split())
        name=input("enter the path of your bin :(Don't use the used name of bin!)")
        output_file = open(name+".bin", 'wb')
        text=input("plaintext/cyphertext=")
        fb=[]
        for i in text :
            i=ord(i)
            i=pow(i,k,n)
            fb.append(i)
        int_array = arr.array('i', fb)  
        int_array.tofile(output_file)
        output_file.close()
    
    def rsa_read() :
        n,k=map(int,input("input your key :(split with space)").split())
        name=input("enter the path of your bin :")
        with open(name + ".bin" , 'rb') as file:
            int_bytes = file.read() 
            for i in int_bytes :
                if i == 0 :
                    continue
                i=pow(i,k,n)
                print(chr(i), end="")


    

    def linr_radom() :  
        text=input("plaintext/cyphertext=")
        LFSR=input("LFSR_4=")
        print()
        print("cyphertext/plaintext=",end='')
        a=int(LFSR[0])
        b=int(LFSR[1])
        c=int(LFSR[2])
        d=int(LFSR[3])
        for i in text :
            print(int(i) ^ a,end="")
            t= a ^ d
            d=a
            a=b
            b=c
            c=t
        print()

    def wood_decry() :
        text=input("input the cryto :")
        n=0
        for i in text :
            if n%4==0 :
                print(i,end="")
            n=n+1
    
    def wood_encry() :
        import random
        text=input("input the plaintext :")
        l=[]
        for i in range(48,122) :
            if (i>48 and i<57) or (i>65 and i<90) or (i>97 and i<122) :
                l.append(i)
        n=0
        for i in text :
            print(i,end="")
            for j in range(3) :
                r=random.choice(l)
                print(chr(r),end="")
            n=n+1
        


    def crytolist() :
        from Option import Option
        optionList = []
        optionList.append(Option(11,"維吉尼亞加密"))
        optionList.append(Option(12,"維吉尼亞解密"))
        optionList.append(Option(13,"RSA加密"))
        optionList.append(Option(14,"RSA加密"))
        optionList.append(Option(15,"RSA建立金鑰"))
        optionList.append(Option(16,"線性亂數加解密"))
        optionList.append(Option(17,"木棒加密"))
        optionList.append(Option(18,"木棒解密"))
        print()


        while(True) :
            os.system('cls')
            for Option in optionList:
                print("[", Option.number-10, "] ", Option.descritpion)
            print("[", 99, "]", "返回")
            selection = input("請輸入需要的功能：").strip()

            print()

            if(selection == "12"):
                cryto.decryp_Vige()
            elif(selection == "11"):
                cryto.encryp_Vige()
            elif(selection == "13"):
                cryto.rsa_send()
            elif(selection == "14"):
                cryto.rsa_read()
            elif(selection == "15"):
                cryto.Make_a_rsa()
            elif(selection == "16"):
                cryto.linr_radom()
            elif(selection == "17"):
                cryto.wood_encry()
            elif(selection == "18"):
                cryto.wood_decry()
            elif(selection == "99"):
                return
            else:
                print("輸入錯誤")