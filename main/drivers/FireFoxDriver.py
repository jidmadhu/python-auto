import logging

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager


class FireFoxDriver:

    def create_driver(self, user_options=None):
        if user_options is None:
            user_options = {}
        options = self.__add_firefoxoption(webdriver.FirefoxOptions())
        if not user_options:
            for op in user_options:
                options.add_argument(op)
        try:
            return webdriver.Firefox(GeckoDriverManager().install())

        except Exception as e:
            logging.warning("Exception while creating the firefox Driver %s ", e.with_traceback)

    def __add_firefoxoption(self, user_options):
        user_options.set_preference("dom.webnotifications.enabled", False)
        user_options.add_argument("--window-size=800,600")
        user_options.add_argument("--no-sandbox")
        user_options.add_argument("--disable-popup-blocking")
        return user_options
