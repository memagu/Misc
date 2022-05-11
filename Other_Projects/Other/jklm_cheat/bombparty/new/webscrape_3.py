from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


def connect(url) -> None:
    driver.get(url)
    s1 = time.perf_counter()
    btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(("xpath", "/html/body/div[2]/div[3]/form/div[2]/button")))
    e1 = time.perf_counter()
    print(f"{btn=} | elapsed time = {e1 - s1}")
    btn.click()

    s2 = time.perf_counter()
    iframe = WebDriverWait(driver, 120).until(EC.presence_of_element_located(("xpath", "//iframe")))
    e2 = time.perf_counter()
    driver.switch_to.frame(iframe)
    print(f"{iframe=} | elapsed time = {e2 - s2}")


def get_syllable() -> str:
    syllable = WebDriverWait(driver, 120).until(EC.visibility_of_element_located(("xpath", "//div[@class='syllable']")))
    return syllable.text


if __name__ == "__main__":
    pass
