import pytest
import allure
from allure_commons._allure import step

from framework.page_forms.spotify_home_form import SpotifyHomeForm
from framework.page_forms.artists_form import ArtistForm
from framework.page_forms.search_song_form import SpotifySearchForm
from framework.tests.conftest import browser


@allure.suite("UI Result")
@pytest.mark.xdist_group(name="UI")
class TestSpotifyUI:
    __spotify_home_form: SpotifyHomeForm = SpotifyHomeForm()
    __artist_form: ArtistForm = ArtistForm()
    __search_song_form: SpotifySearchForm = SpotifySearchForm()

    @pytest.mark.parametrize("artist, song", [
        ("Drake", "One Dance"),
        ("The Beatles", "Here Comes The Sun - Remastered 2009")
    ])
    @allure.feature("Searching artists with specific song")
    @allure.story("Tests for finding songs in artists")
    @step("Testing artists song")
    def test_artist_song(self, artist, song, browser):
        self.__spotify_home_form.click_search_btn()
        self.__spotify_home_form.input_search_field(artist)
        assert self.__artist_form.is_song_exists(song), f"{artist}'s {song} was not found"

        allure.attach(browser.driver.get_screenshot_as_png(), name=f"{artist}_{song}_screenshot",
                      attachment_type=allure.attachment_type.PNG)

    @pytest.mark.parametrize("artist", [
        "Drake",
        "The Beatles"
    ])
    @pytest.mark.skip(reason="This feature currently not working properly")
    def test_recent_search(self, artist):
        self.__spotify_home_form.click_search_btn()
        assert self.__search_song_form.recent_search(artist)
