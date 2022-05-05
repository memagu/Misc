from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

url = "https://jklm.fun/PVVP"
driver.get(url)

s1 = time.perf_counter()
btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", "/html/body/div[2]/div[3]/form/div[2]/button")))
e1 = time.perf_counter()
print(f"{btn=} | elapsed time = {e1 - s1}")
btn.click()

s2 = time.perf_counter()
iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located(("xpath", "//iframe[@src='https://falcon.jklm.fun/games/bombparty']")))
e2 = time.perf_counter()
driver.switch_to.frame(iframe)
print(f"{iframe=} | elapsed time = {e2 - s2}")

while True:
    s3 = time.perf_counter()
    syllable = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(("xpath", "/html/body/div[2]/div[2]/div[2]/div[2]/div[@class='syllable']")))
    e3 = time.perf_counter()
    # print(f"{syllable=} | elapsed time = {e3 - s3}")

    print(syllable.text)
    time.sleep(0.25)



