from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_session_storage_auth():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 20)
    base = "https://gitflic.ru/"
    driver.get(base)  # обязательно открыть домен перед добавлением cookie
    # COOKIE для пользователей
    USER1_COOKIES = [
        {"name": "SESSION",
         "value": "Y2NkYmVmNjgtMzg4OS00OTE4LTk4MzgtNjk3YjQ4MzY5MWEw",
         "path": "/"}
    ]
    USER2_COOKIES = [
        {"name": "SESSION",
         "value": "M2FmNzNjNWYtMGM4OC00YWE2LTljYzMtM2Q1MjhhOTY2ODg1",
         "path": "/"}
    ]

    # Очистим существующие cookie и установим cookie пользователя 1
    driver.delete_all_cookies()
    for c in USER1_COOKIES:
        driver.add_cookie({k: c[k] for k in ("name", "value", "path",
                                             "domain", "expiry", "secure",
                                             "httpOnly") if k in c})
    driver.refresh()  # применить cookie

    # Перейти на профиль пользователя 1
    PROFILE1 = base + "sunshine19_87"
    driver.get(PROFILE1)
    wait.until(EC.url_contains("sunshine19_87"))
    url1 = driver.current_url

    # Разлогиниться — удалить все cookie и обновить страницу
    driver.delete_all_cookies()
    driver.refresh()

    # Установить cookie пользователя 2
    for c in USER2_COOKIES:
        driver.add_cookie({k: c[k] for k in ("name", "value", "path",
                                             "domain", "expiry", "secure",
                                             "httpOnly") if k in c})
    driver.refresh()

    # Перейти на профиль пользователя 2
    PROFILE2 = base + "belka"
    driver.get(PROFILE2)
    wait.until(EC.url_contains("belka"))
    url2 = driver.current_url

    # Проверка: URLы должны различаться
    assert url1 != url2, f"{url1}"

    driver.quit()
