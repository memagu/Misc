from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


def wait_and_click(driver: webdriver.Chrome, button_xpath: str) -> None:
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", button_xpath))).click()


def main() -> None:
    urls = ("https://soundcloud.com/doucer/eliza-rose-baddest-of-them-all-doucer-remix-1",
            "https://soundcloud.com/doucer/22-above")

    for i in range(1, 10):
        with webdriver.Chrome(service=Service(ChromeDriverManager().install())) as driver:
            driver.get(urls[i % len(urls)])
            wait_and_click(driver, "/html/body/div[2]/div[2]/div/div[1]/div/div[2]/div/button[1]")
            wait_and_click(driver, "/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div[1]/a")


if __name__ == "__main__":
    main()
