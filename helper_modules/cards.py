from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class CardsHelper:
    def __init__(self, app):
        self.app = app
        self.driver = self.app.driver
        self.window_handle = {}

    def open_cards_page(self) -> None:
        if self.driver.current_url.endswith("cards"):
            return
        link = self.driver.find_element(By.LINK_TEXT, "Карты")
        ActionChains(self.driver).key_down(Keys.CONTROL).click(link).key_up(Keys.CONTROL).perform()
        self.window_handle["cards"] = self.driver.window_handles[-1]
        self.switch_to_page()

    def switch_to_page(self):
        if "cards" in self.window_handle:
            self.driver.switch_to.window(self.window_handle["cards"])

    def close_card_page(self):
        if "cards" in self.window_handle:
            self.driver.switch_to.window(self.window_handle["cards"])
            self.driver.close()
            del self.window_handle["cards"]
