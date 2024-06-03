import os
import json
import logging


class ApiConstants:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    RESOURCE_FILE_PATH = os.path.join(BASE_DIR, '..', '..', 'resources')
    API_CONSTANTS_PATH = os.path.join(RESOURCE_FILE_PATH, 'api_constants.json')
    ERROR_MSG = "API constants file not found or incorrect"

    @staticmethod
    def load_api_constants():
        try:
            with open(ApiConstants.API_CONSTANTS_PATH, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            logging.error(ApiConstants.ERROR_MSG)
            raise

    @staticmethod
    def get_http_status_constants():
        constants = ApiConstants.load_api_constants()
        return constants.get('HttpStatusConstants')

    @staticmethod
    def get_endpoint_constants():
        constants = ApiConstants.load_api_constants()
        return constants.get('EndPointConstants')