import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="session")
def browser():
    options = Options()
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome(executable_path="C:\chromedriver\chromedriver.exe", options=options)
    yield driver
    driver.quit()


