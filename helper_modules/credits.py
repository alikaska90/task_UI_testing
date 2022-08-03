import time
from selenium.webdriver.common.by import By


class CreditsHelper:
    def __init__(self, app):
        self.app = app
        self.driver = self.app.driver
        self.is_opened = False

    def open_credit_page(self):
        if self.driver.current_url.endswith("credits"):
            return
        self.driver.find_element(By.LINK_TEXT, "Кредиты").click()
        self.is_opened = True

    def download_file_remainder_ib(self):
        if not self.is_opened:
            self.open_credit_page()
        self.driver.find_element(By.CSS_SELECTOR, ".mb-5:nth-child(2)").click()
        time.sleep(5)
