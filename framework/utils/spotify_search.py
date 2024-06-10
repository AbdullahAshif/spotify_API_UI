import requests
from requests.auth import HTTPBasicAuth
from framework.utils.settings_api_data import ApiConstants
from config import CLIENT_ID, CLIENT_SECRET

HttpStatusConstants = ApiConstants.get_http_status_constants()
EndPointConstants = ApiConstants.get_endpoint_constants()


class SpotifyApiSearch:
    def __init__(self):
        self.token = self.__get_access_token()

    @staticmethod
    def __get_access_token():
        response = requests.post(
            EndPointConstants['TOKEN_URL_LOCATOR'],
            data={"grant_type": "client_credentials"},
            auth=HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)
        )
        if response.status_code != HttpStatusConstants['OK']:
            raise ConnectionError("Failed to authenticate with Spotify API")
        return response.json()["access_token"]

    def get_headers(self):
        return {"Authorization": f"Bearer {self.token}"}

    def get_artist(self, artist_name):
        response = requests.get(
            EndPointConstants['SEARCH_ENDPOINT'],
            headers=self.get_headers(),
            params={"q": artist_name, "type": "artist"}
        )
        if response.status_code != HttpStatusConstants['OK']:
            raise ConnectionError("Failed to get artist data!")
        return response.json()["artists"]["items"][0]

    def get_artist_top_tracks(self, artist_id):
        response = requests.get(
            f"{EndPointConstants['BASE_API_EP_LOCATOR']}/artists/{artist_id}/top-tracks",
            headers=self.get_headers(),
            params={"market": "US"}
        )
        if response.status_code != HttpStatusConstants['OK']:
            raise ConnectionError("Failed to get artists' tracks data!")
        return response.json()["tracks"]
