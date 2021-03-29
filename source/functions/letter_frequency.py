from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
def frequency():
    
    str1=input("輸入字串")
    res = ''.join(sorted(str1))  
    letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    chars_in_string = Counter(res)
    res = {}
    for letter in letters:
        if(letter in chars_in_string):
            res[letter] = chars_in_string[letter]
        else: 
            res[letter] = 0 
    #print(res)
    plt.bar(range(len(res)), list(res.values()), align='center')
    plt.xticks(range(len(res)), list(res.keys()))

    plt.show()
    