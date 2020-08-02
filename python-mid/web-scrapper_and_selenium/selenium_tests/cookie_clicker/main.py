import unittest
import page
from selenium import webdriver


class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://www.python.org')

    def test_title(self):
        main_page = page.MainPage(self.driver)
        assert main_page.is_title_match()

    def test_search_python(self):
        main_page = page.MainPage(self.driver)
        assert main_page.is_title_match()
        main_page.search_text_element = 'pycon'
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_result_found()

    def tearDown(self) -> None:
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
