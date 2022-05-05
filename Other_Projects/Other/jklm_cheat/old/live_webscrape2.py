import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
url = "https://jklm.fun/PVVP"
# url = "https://falcon.jklm.fun/games/bombparty"
driver = webdriver.Chrome(os.path.dirname(__file__) + "\\chromedriver.exe")
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url)

response = driver.execute_script("return document.documentElement.outerHTML")
print(response)

# while True:
#     hint = driver.find_element("xpath", "/html/body/div[2]/div[2]/div[2]/div[2]/div")
#     print(hint)
#     time.sleep(0.5)

