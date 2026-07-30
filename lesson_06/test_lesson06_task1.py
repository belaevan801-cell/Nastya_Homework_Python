from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    driver = webdriver.Chrome()
    # 1. Откройте страницу
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
    # 2. Найдите и нажмите на кнопку "Start"
    start_btn = driver.find_element(By.CSS_SELECTOR, "#start button")
    start_btn.click()

    # 3. Дождитесь появления текста "Hello World!"
    wait = WebDriverWait(driver, 15)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#finish")))

    # 4. Сделайте скриншот страницы
    driver.save_screenshot("dynamic_loading_result.png")

    # 5. Проверьте, что появившийся текст равен "Hello World!"
    result_text = driver.find_element(By.CSS_SELECTOR, "#finish").text
    assert result_text == "Hello World!"

    driver.quit()
