from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


def connect(url) -> None:
    driver.get(url)
    s1 = time.perf_counter()
    btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(("xpath", "/html/body/div[2]/div[3]/form/div[2]/button")))
    e1 = time.perf_counter()
    # print(f"{btn=} | elapsed time = {e1 - s1}")
    btn.click()

    s2 = time.perf_counter()
    # iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located(("xpath", "//iframe[@src='https://falcon.jklm.fun/games/bombparty']")))
    iframe = WebDriverWait(driver, 120).until(EC.presence_of_element_located(("xpath", "//iframe")))
    e2 = time.perf_counter()
    driver.switch_to.frame(iframe)
    # print(f"{iframe=} | elapsed time = {e2 - s2}")


def get_syllable() -> str:
    syllable = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(("xpath", "//div[@class='syllable']")))
    return syllable.text


def enter_word(word: str) -> None:
    driver.find_element("xpath", "")


if __name__ == "__main__":
    connect("https://jklm.fun/QFXK")
    while True:
        if driver.find_element("xpath", "//input[@class='styled']"):
            driver.find_element("xpath", "//input[@class='styled']").send_keys("test" + Keys.ENTER)
