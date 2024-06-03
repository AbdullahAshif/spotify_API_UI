import pytest
from framework.page_forms.spotify_home_form import SpotifyHomeForm
from framework.page_forms.artists_form import ArtistForm
from framework.page_forms.search_song_form import SpotifySearchForm
from framework.tests.base_test import prepare_browser_factory


class TestSpotifyUI:
    @pytest.fixture(scope="class")
    def spotify_home_form(self, prepare_browser_factory):
        return SpotifyHomeForm()

    @pytest.fixture(scope="class")
    def artist_form(self, prepare_browser_factory):
        return ArtistForm()

    @pytest.fixture(scope="class")
    def search_song_form(self, prepare_browser_factory):
        return SpotifySearchForm()

    @pytest.mark.parametrize("artist, song", [
        ("Drake", "One Dance"),
        ("The Beatles", "Here Comes The Sun - Remastered 2009")
    ])
    def test_artist_song(self, spotify_home_form, artist_form, artist, song):
        spotify_home_form.click_search_btn()
        spotify_home_form.input_search_field(artist)
        assert artist_form.is_song_exists(song), f"{artist}'s {song} was not found"

    @pytest.mark.parametrize("artist", [
        "Drake",
        "The Beatles"
    ])
    @pytest.mark.skip(reason="This feature currently not working properly")
    def test_recent_search(self, spotify_home_form, search_song_form, artist):
        spotify_home_form.click_search_btn()
        assert search_song_form.recent_search(artist)
