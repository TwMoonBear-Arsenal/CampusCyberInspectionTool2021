from FuncBase import FuncBase
import webbrowser


class Openyt(FuncBase):

    @property
    def Description(self):
        return("開啟Youtube")

    def Run(self):
        urL = 'https://www.youtube.com/'
        chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        webbrowser.register(
            'chrome', None, webbrowser.BackgroundBrowser(chrome_path))
        webbrowser.get('chrome').open_new(urL)
