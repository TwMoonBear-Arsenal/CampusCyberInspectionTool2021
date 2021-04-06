from FuncBase import FuncBase
from datetime import datetime

# 時鐘(繼承功能基底類別)


class ClockFunc(FuncBase):

    # 實作屬性
    @property
    def Description(self):
        return '顯示今天日期'

    # 實作執行
    def Run(self):

        # 告知目前時間
        print(datetime.now())
