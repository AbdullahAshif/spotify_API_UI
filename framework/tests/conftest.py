import pytest
from framework.utils.spotify_search import SpotifyApiSearch


@pytest.fixture(scope="session")
def spotify_api_client():
    return SpotifyApiSearch()
