from selenium import webdriver
from helper_modules.search_engine import SearchEngineHelper
from helper_modules.halva import HalvaHelper
from helper_modules.cards import CardsHelper
from helper_modules.credits import CreditsHelper
import os.path

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_DIR = os.path.join(ROOT_DIR, "downloads")
options = webdriver.ChromeOptions()
prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': FILE_DIR}
options.add_experimental_option('prefs', prefs)


class Application:
    def __init__(self):
        self.driver = webdriver.Chrome(chrome_options=options)
        self.search_engine = SearchEngineHelper(self)
        self.cards = CardsHelper(self)
        self.halva = HalvaHelper(self)
        self.credits = CreditsHelper(self)

    def session_is_valid(self) -> bool:
        try:
            self.driver.current_url
            return True
        except:
            return False

    def session_destroy(self) -> None:
        self.driver.quit()
