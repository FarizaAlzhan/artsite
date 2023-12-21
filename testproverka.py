import warnings

from selenium import webdriver
import unittest

class UrlTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url = "http://127.0.0.1:8000"  # Замените на ваш базовый URL

    def tearDown(self):
        self.driver.quit()

    def test_home_page(self):
        url = self.base_url + '/'
        self.assertTrue(self.check_url(url), f"Failed for URL: {url}")

    def test_about_page(self):
        url = self.base_url + '/about/'
        self.assertTrue(self.check_url(url), f"Failed for URL: {url}")

    def check_url(self, url):
        try:
            self.driver.get(url)
            return print('Тест успешно прошел')
        except Exception as e:
            print(f"Error accessing URL: {url}")
            print(f"Exception: {e}")
            return False

if __name__ == '__main__':

    with warnings.catch_warnings():
        warnings.simplefilter("ignore", ResourceWarning)
        unittest.main()
