import time
import unittest

from main.drivers.ChromeDriver import ChromeDriver


class ChromeDriverTest(unittest.TestCase):

    def test_get_chrome_browser(self):
        test = ChromeDriver().create_driver()
        test.get("http://www.google.com")
        self.assertTrue(test.find_element_by_name("q").is_displayed())
        search_box = test.find_element_by_name("q")
        search_box.send_keys("Ganapathi")
        search_box.submit()
        time.sleep(3)
        test.quit()


if __name__ == '__main__':
    unittest.main()
