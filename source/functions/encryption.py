class cryto:

    def encryp_Vige() :
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

