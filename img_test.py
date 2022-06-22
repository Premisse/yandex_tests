from YandexPages import SearchHelper


def test_img_button(browser):
    yandex_main_page = SearchHelper(browser)
    yandex_main_page.go_to_site()
    element = yandex_main_page.check_navigation_img()
    assert element

def test_img_url(browser):
    yandex_main_page = SearchHelper(browser)
    yandex_main_page.go_to_site()
    yandex_main_page.click_on_the_images_button()
    window_url = yandex_main_page.check_page_url()
    assert "https://yandex.ru/images/" in window_url



