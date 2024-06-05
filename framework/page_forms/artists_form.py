from forms.base_form import BaseForm
from resources.locator_constants import LocatorConstants
from browser.py_quality_services import PyQualityServices
from selenium.webdriver.common.by import By


class ArtistForm(BaseForm):
    __form_name = "Top result"
    __element = PyQualityServices.element_factory

    def __init__(self):
        super(ArtistForm, self).__init__((By.XPATH, LocatorConstants.PRECISE_TEXT_XPATH.format(self.__form_name)),
                                         self.__form_name)

    def is_song_exists(self, song_name):
        song_name = self.__element.get_label((By.XPATH, LocatorConstants.PARTICULAR_TEXT_XPATH.format(song_name)),
                                             "Song")
        return song_name.state.is_displayed
