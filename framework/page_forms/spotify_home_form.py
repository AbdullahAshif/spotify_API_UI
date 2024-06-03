from forms.base_form import BaseForm
from browser.py_quality_services import PyQualityServices
from selenium.webdriver.common.by import By
from resources.locator_constants import LocatorConstants


class SpotifyHomeForm(BaseForm):
    __form_name = "Popular artists"
    __element = PyQualityServices.element_factory
    __search_btn = __element.get_button((By.XPATH, ("//*[contains(@class, 'search')]")), "Search Button")
    __search_box = __element.get_text_box(
        (By.XPATH, ("//*[contains(@class, 'encore-text') and contains(@data-testid, 'search-input')]")), "Search")
    __log_in_btn = __element.get_button(
        (By.XPATH, ("//*[@id= 'main']//button[2]//span[contains(@class, 'ButtonInner')]")), "Log in button")

    def __init__(self):
        super(SpotifyHomeForm, self).__init__((By.XPATH, LocatorConstants.PRECISE_TEXT_XPATH.format(self.__form_name)),
                                              self.__form_name)

    def click_search_btn(self):
        self.__search_btn.click()

    def input_search_field(self, singer_name):
        self.__search_box.clear_and_type(singer_name)

    def click_log_in_btn(self):
        self.__log_in_btn.click()

    def is_displayed(self):
        return self.state.wait_for_not_displayed
