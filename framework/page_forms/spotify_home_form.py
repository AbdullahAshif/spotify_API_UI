from forms.base_form import BaseForm
from browser.py_quality_services import PyQualityServices
from selenium.webdriver.common.by import By
from resources.locator_constants import LocatorConstants


class SpotifyHomeForm(BaseForm):
    __form_name = "Popular artists"

    def __init__(self):
        super(SpotifyHomeForm, self).__init__((By.XPATH, LocatorConstants.PRECISE_TEXT_XPATH.format(self.__form_name)),
                                              self.__form_name)
        self.__search_btn = self._element_factory.get_button((By.XPATH, ("//*[contains(@class, 'search')]")), "Search")
        self.__search_box = self._element_factory.get_text_box(
        (By.XPATH, ("//*[contains(@class, 'encore-text') and contains(@data-testid, 'search-input')]")), "Search")
        self.__log_in_btn = self._element_factory.get_button(
        (By.XPATH, ("//span[contains(@class, 'ButtonInner') and text()='Log in']")), "Log in")

    def click_search_btn(self):
        self.__search_btn.click()

    def input_search_field(self, singer_name):
        self.__search_box.clear_and_type(singer_name)

    def click_log_in_btn(self):
        self.__log_in_btn.click()
