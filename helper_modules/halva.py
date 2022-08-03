from selenium.webdriver.common.by import By


class HalvaHelper:
    def __init__(self, app):
        self.app = app
        self.driver = self.app.driver
        self.window_handle = {}
        self.is_opened = False
        self.checkbox_message = ""
        self.field_messages = {}

    def click_halva_request(self) -> None:
        if self.is_opened:
            return
        self.app.cards.open_cards_page()
        halva_button = self.driver.find_element(By.XPATH, "//a[contains(text(),'Заказать халву')]")
        halva_button.click()
        self.window_handle["halva"] = self.driver.window_handles[-1]
        self.app.cards.close_card_page()
        self.driver.switch_to.window(self.window_handle["halva"])
        self.is_opened = True

    def close_page(self):
        if "halva" in self.window_handle:
            self.driver.switch_to.window(self.window_handle["halva"])
            self.driver.close()
            self.is_opened = False
            del self.window_handle["halva"]

    def click_checkbox_agree(self) -> None:
        if not self.is_opened:
            self.click_halva_request()
        self.driver.find_element(By.NAME, "agree").click()

    def check_status_checkbox_agree(self) -> bool:
        if not self.is_opened:
            raise ValueError("Halva page is not opened")
        element = self.driver.find_element(By.NAME, "agree")
        return element.is_selected()

    def click_get_card_button(self) -> None:
        if not self.is_opened:
            raise ValueError("Halva page is not opened")
        self.driver.find_element(By.CSS_SELECTOR, ".formBtn > .MuiButton-label").click()

    def get_status_messages(self, element: str) -> bool:
        all_field_messages = True
        card_form = self.driver.find_element(By.CSS_SELECTOR, "div.jss27")
        form_fields = card_form.find_elements(By.XPATH, "./div")
        if element == "checkbox":
            try:
                self.checkbox_message = form_fields[4].find_element(By.XPATH, ".//p").text
            except:
                return False
        elif element == "fields":
            for i in range(4):
                try:
                    key = form_fields[i].find_element(By.XPATH, ".//label").text
                    message = form_fields[i].find_element(By.XPATH, ".//p").text
                    self.field_messages[key] = message
                except:
                    all_field_messages = False
        else:
            raise ValueError("Unexpected element")
        return all_field_messages
