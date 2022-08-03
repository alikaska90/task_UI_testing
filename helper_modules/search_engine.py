from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class SearchEngineHelper:
    def __init__(self, app):
        self.driver = app.driver
        self.window_handle = {}
        self.is_opened = False
        self.is_found = False

    def open_search_engine(self) -> None:
        self.driver.get("https://www.google.com/")
        self.window_handle["search_engine"] = self.driver.current_window_handle
        self.is_opened = True

    def close_search_engine(self) -> None:
        if "search_engine" in self.window_handle:
            self.driver.switch_to.window(self.window_handle["search_engine"])
            self.driver.close()
            del self.window_handle["search_engine"]
            self.is_opened = False

    def request_execution(self, request_string: str) -> None:
        if "search_engine" in self.window_handle:
            self.driver.switch_to.window(self.window_handle["search_engine"])
            self.driver.find_element(By.NAME, "q").send_keys(request_string)
            self.driver.find_element(By.NAME, "q").send_keys(Keys.ENTER)
            self.is_found = True

    def open_website(self) -> None:
        link = self.driver.find_element(By.XPATH, "//cite[contains(text(), 'https://sovcombank.ru')]")
        ActionChains(self.driver).key_down(Keys.CONTROL).click(link).key_up(Keys.CONTROL).perform()
        self.window_handle["website"] = self.driver.window_handles[-1]

    def switch_to_website(self) -> None:
        if "website" in self.window_handle:
            self.driver.switch_to.window(self.window_handle["website"])

    def number_of_found_results(self) -> str:
        if not self.is_found:
            return "Current page doesn't have found results"
        return self.driver.find_element(By.ID, "result-stats").text
