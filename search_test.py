from YandexPages import SearchHelper


def test_input_field(browser):
    yandex_main_page = SearchHelper(browser)
    yandex_main_page.go_to_site()
    element = yandex_main_page.find_area()
    assert element

def test_dropdown_list(browser):
    yandex_main_page = SearchHelper(browser)
    yandex_main_page.go_to_site()
    yandex_main_page.enter_word('Тензор')
    element = yandex_main_page.drop_down_list()
    assert element

def test_search_results(browser):
    yandex_main_page = SearchHelper(browser)
    yandex_main_page.go_to_site()
    yandex_main_page.enter_word('Тензор')
    yandex_main_page.click_on_the_search_button()
    element = yandex_main_page.check_results()
    assert element

def test_first_result(browser):
    yandex_main_page = SearchHelper(browser)
    yandex_main_page.go_to_site()
    yandex_main_page.enter_word('Тензор')
    yandex_main_page.click_on_the_search_button()
    element = yandex_main_page.check_first_result()
    assert element

