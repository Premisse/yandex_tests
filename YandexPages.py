from BaseApp import BasePage
from selenium.webdriver.common.by import By

class YandexSeacrhLocators:
    LOCATOR_YANDEX_SEARCH_TEXTFIELD = (By.ID, "text")
    LOCATOR_YANDEX_SEARCH_BUTTON = (By.CLASS_NAME, "search2__button")
    LOCATOR_YANDEX_SUGGEST = (By.CSS_SELECTOR, ".mini-suggest__item")
    LOCATOR_YANDEX_RESULTS = (By.ID, "search-result")
    LOCATOR_YANDEX_FIRST_RESULT = (By.XPATH, "//li[@data-cid='0']//a[@href='https://tensor.ru/']")
    LOCATOR_YANDEX_SEARCH_IMG_FIELD = (By.XPATH, "//a[@data-id='images']")
    LOCATOR_YANDEX_WINDOW = ()



class SearchHelper(BasePage):

    def find_area(self):
        search_field = self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_TEXTFIELD)
        return search_field

    def enter_word(self, word):
        search_field = self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_TEXTFIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def drop_down_list(self):
        return self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_SUGGEST)

    def click_on_the_search_button(self):
        return self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_BUTTON, time=2).click()

    def check_results(self):
        return self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_RESULTS)

    def check_first_result(self):
        return self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_FIRST_RESULT)

    def check_navigation_img(self):
        return self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_IMG_FIELD)

    def click_on_the_images_button(self):
        return self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_IMG_FIELD, time=6).click()

    def check_page_url(self):
        return self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_WINDOW)





