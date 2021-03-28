import time
import unittest

from drivermanager.DriverManager import DriverManager


class DriverManagerTest(unittest.TestCase):

    def test_chromeBrowser(self):
        test = DriverManager().get_driver("chrome")
        test.get("http://www.google.com")
        self.assertTrue(test.find_element_by_name("q").is_displayed())
        search_box = test.find_element_by_name("q")
        search_box.send_keys("Ganapathi")
        search_box.submit()
        time.sleep(3)
        test.quit()


if __name__ == '__main__':
    unittest.main()
