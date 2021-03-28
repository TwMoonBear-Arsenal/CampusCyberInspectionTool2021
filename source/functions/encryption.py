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
            if   p > 1 : #查看因子 
                t=0
                for   i   in   range ( 2 , p ) : 
                    if   ( p % i ) == 0 : 
                        print ( "請輸入質數",end="")
                        t=1
                        break
                if t == 1 :
                    continue    
            if   q > 1 : #查看因子 
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

    def rsa_pp() :
        import math
        n,k=map(int,input("input your key :(split with space)").split())
        text=input("plaintext/cyphertext=")
        for i in text :
            i=ord(i)
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

        