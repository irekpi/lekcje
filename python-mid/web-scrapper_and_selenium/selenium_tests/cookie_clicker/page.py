from locators import *
from elements import BasePageElement


class SearchTextElement(BasePageElement):
    locator = 'q'


class BasePage:
    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    search_text_element = SearchTextElement

    def is_title_match(self):
        return "Python" in self.driver.title

    def click_go_button(self):
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element.click()


class SearchResultPage(BasePage):

    def is_result_found(self):
        return "Not found a match" not in self.driver.page_source
