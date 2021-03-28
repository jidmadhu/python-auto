from drivers.ChromeDriver import ChromeDriver
from drivers.FireFoxDriver import FireFoxDriver


class DriverManager:
    __browser = "chrome"
    __run_type = "local"

    def __int__(self, browser="chrome", run_type="local"):
        self.__browser = browser
        self.__runType = run_type

    def get_driver(self, browser):
        self.__browser = "chrome" if browser is None else browser
        return self.__getbrowser(self.__browser)

    def __getbrowser(self, i):
        browser = {"chrome": ChromeDriver().create_driver() if self.__browser == "chrome" else None,
                   "firefox": FireFoxDriver().create_driver() if self.__browser == "firefox" else None}
        return browser.get(i, "This browser not supported, Please give " + browser.values().__str__())

    def chrome(self):
        return
