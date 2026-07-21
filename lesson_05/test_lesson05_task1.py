import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    # Инициализация драйвера — тело функции должно быть с отступом
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_navigation(driver):
    driver.get("https://httpbin.org/")
    original_url = driver.current_url

    driver.find_element(By.LINK_TEXT, "HTML Form").click()

    WebDriverWait(driver, 10).until(EC.url_contains("/forms/post"))
    assert "/forms/post" in driver.current_url

    driver.back()

    WebDriverWait(driver, 10).until(EC.url_to_be(original_url))
    assert driver.current_url == original_url
