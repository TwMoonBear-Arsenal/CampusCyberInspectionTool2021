import argparse
import os
import webbrowser
#import nmap
from Option import Option
from functions.Clock import Clock
from functions.shut import shut
from functions.Ipconfig import Showip
import functions.sqlmap


def main():
    # 準備參數解析
    app_description = "校園資安測試常用工具集合"
    epilog_text = "歡迎至https://github.com/TwMoonBear-Arsenal/BetterCalculator/issues提供建議"
    parser = argparse.ArgumentParser(
        description=app_description, epilog=epilog_text)
    args = parser.parse_args()

    # 準備選單
    optionList = []
    optionList.append(Option(1, "顯示今天日期"))
    optionList.append(Option(2,"find my ip"))
    optionList.append(Option(87,"simple stu.sqlmap"))
    optionList.append(Option(878,"stu.sqlmap guide"))
    print()
    lasttarget = 'no last target'
    while(True):

        # 顯示選單
        os.system('cls')
        print(app_description)
        print(epilog_text)
        print("--------")
        for option in optionList:
            print("[", option.number, "] ", option.descritpion)
        print("[", 99, "]", " 結束程式")

        # 詢問使用者
        selection = input("請輸入需要的功能：").strip()
        if(selection == "1"):
            Clock.ShowTime()
        elif(selection == "2"):
            Showip.ipconfig()
        elif(selection == "87"):
            os.system("cls")
            print("your last target:" + lasttarget)
            target = input("target site:")
            lasttarget = target
            target2 = "python .\\source\\functions\sqlmap\sqlmap.py \\\""+target+"\" "
            os.system('cls')
            print("your target:"+target)
            optionList2 = []
            optionList2.append(Option(1,"爆破"))
            optionList2.append(Option(2,"找資料庫DataBase"))
            optionList2.append(Option(3,"找使用者"))
            optionList2.append(Option(4,"找密碼"))
            for option in optionList2:
                print("[", option.number, "] ", option.descritpion)
            selection2=input("do what:")
            if(selection2 == '1'):
                target3 = target2 + "--batch"
                os.system(target3)
            elif(selection2 == '2'):
                target3 = target2 + "--dbs"
                os.system(target3)
            elif(selection2 == '3'):
                target3 = target2 + "--current-user"
                os.system(target3)
            elif(selection2 == '4'):
                target3 = target2 + "--passwords"
                os.system(target3)
            else:
                print("輸入錯誤")
                pass
        elif(selection == "878"):
            target = "python .\\source\\functions\sqlmap\sqlmap.py -h"
            os.system(target)
        elif(selection == "99"):
            print("See you next time...")
            print()
            return
        else:
            print("輸入錯誤")

        # 開始下一循環
        input("按任意鍵繼續...")


if __name__ == "__main__":
    main()
