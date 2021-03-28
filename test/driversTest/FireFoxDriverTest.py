import time
import unittest

from main.drivers.FireFoxDriver import FireFoxDriver


class MyTestCase(unittest.TestCase):

    def test_get_firefox_browser(self):
        test = FireFoxDriver().create_driver()
        test.get("http://www.google.com")
        self.assertTrue(test.find_element_by_name("q").is_displayed())
        search_box = test.find_element_by_name("q")
        search_box.send_keys("Ganapathi")
        search_box.submit()
        time.sleep(3)
        test.quit()


if __name__ == '__main__':
    unittest.main()
