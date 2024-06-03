import os
import json
import logging


class SettingsData:
    # Dynamically determine the absolute path to the resources directory
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    RESOURCE_FILE_PATH = os.path.join(BASE_DIR, '..', '..', 'resources')
    ENV_FILE_PATH = os.path.join(RESOURCE_FILE_PATH, 'env.json')
    PROD_FILE_PATH = os.path.join(RESOURCE_FILE_PATH, 'prod.json')
    ERROR_MSG = "File with environment settings not found or incorrect"
    ERROR_FILE_READ_MSG = "Environment file not found"

    @staticmethod
    def get_environment():
        try:
            with open(SettingsData.ENV_FILE_PATH, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            logging.error(SettingsData.ERROR_MSG)
            raise

    @staticmethod
    def get_env_data():
        try:
            env = SettingsData.get_environment().get('env')
            if env == "prod":
                with open(SettingsData.PROD_FILE_PATH, 'r') as f:
                    return json.load(f)
            logging.info("Env is not set")
            raise RuntimeError(SettingsData.ERROR_MSG)
        except FileNotFoundError:
            logging.error(SettingsData.ERROR_FILE_READ_MSG + " at: " + SettingsData.PROD_FILE_PATH)
            raise
