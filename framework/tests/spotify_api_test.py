import pytest
import allure
import json
from framework.models.artist import Artist


@allure.suite("API Result")
@pytest.mark.xdist_group(name="API")
class TestApi:
    @pytest.mark.parametrize("artist_name, expected_genre", [
        ("Drake", "Rap"),
        ("The Beatles", "British Invasion")
    ])
    @allure.feature("Searching Artists with Genre")
    @allure.story("Tests for finding genre of Artists")
    def test_artist_genre(self, spotify_api_client, artist_name, expected_genre):
        with allure.step(f"Fetching {artist_name} info from spotify"):
            artist = spotify_api_client.get_artist(artist_name)
            allure.attach(json.dumps(artist), name="artist_data", attachment_type=allure.attachment_type.JSON)
        with allure.step("Fetching genre of artist"):
            genres = [genre.lower() for genre in artist["genres"]]
            allure.attach(json.dumps(genres), name="genres_data", attachment_type=allure.attachment_type.JSON)
        with allure.step(f"Asserting expected genre is in the genre-list of the {artist_name}"):
            assert expected_genre.lower() in genres, f"Expected {expected_genre} in {artist['genres']}"


    @pytest.mark.parametrize("artist_name, expected_song", [
        ("Drake", "One Dance"),
        ("The Beatles", "Here Comes The Sun - Remastered 2009")
    ])
    @allure.feature("Searching Artists with Song")
    @allure.story("Tests for finding specific song from Artists")
    def test_artist_songs(self, spotify_api_client, artist_name, expected_song):
        with allure.step(f"Fetching {artist_name} info from spotify"):
            artist = spotify_api_client.get_artist(artist_name)
            allure.attach(json.dumps(artist), name="artist_data", attachment_type=allure.attachment_type.JSON)
        with allure.step(f"Fetching top-tracks of the {artist_name}"):
            top_tracks = spotify_api_client.get_artist_top_tracks(artist["id"])
            allure.attach(json.dumps(top_tracks), name="artist_top_tracks", attachment_type=allure.attachment_type.JSON)
        song_names = [track["name"] for track in top_tracks]
        with allure.step(f"Asserting expected song is in the song-list of the {artist_name}"):
            assert expected_song in song_names, f"Expected {expected_song} in {song_names}"
