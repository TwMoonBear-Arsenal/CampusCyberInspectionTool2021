import argparse  # 參數解析使用
import os
from Option import Option
from functions.Clock import Clock
from functions.encryption import cryto
from functions.shut import shut
from functions.Ipconfig import Showip
import webbrowser



def main():
    # 準備參數解析
    app_description = "校園資安測試常用工具集合"
    epilog_text = "歡迎至https://github.com/TwMoonBear-Arsenal/BetterCalculator/issues提供建議"
    parser = argparse.ArgumentParser(
        description=app_description, epilog=epilog_text)
    args = parser.parse_args()

    # 準備選單
    optionList = []
    optionList.append(Option("1","顯示今天日期"))
    optionList.append(Option("2","顯示本地端IP地址"))
    optionList.append(Option("3","加解密工具"))
    print()

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
        print()
        if(selection == "1"):
            Clock.ShowTime()
        elif(selection == '2'):
            Showip.ipconfig()
        elif(selection == '3') :
            cryto.crytolist()
        elif(selection == "77"):
            shut.shut()
        elif(selection == "87"):
            webbrowser.open("https://www.facebook.com/simon.lin.56829")
            for i in range(1,100):
               print('878787878787 "Simon" db2')
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
