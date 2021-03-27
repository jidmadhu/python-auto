"""
@author: Jidhu Madhu
"""

import logging

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class ChromeDriver:

    def create_driver(self, user_options={}):
        try:
            options = self.__add_chromeoption(webdriver.ChromeOptions())
            if not user_options:
                for op in user_options:
                    options.add_argument(op)
            return webdriver.Chrome(ChromeDriverManager().install())

        except Exception as e:
            logging.warning("File Not Found Exception %s ", e.with_traceback)

    def __add_chromeoption(self, user_options):
        user_options.add_argument("--disable-dev-shm-usage")
        user_options.add_argument("--window-size=800,600")
        user_options.add_argument("--no-sandbox")
        user_options.add_argument("--disable-popup-blocking")
        return user_options
