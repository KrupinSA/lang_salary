import logging

import dotenv
import requests

logger = logging.getLogger(__name__)

def main():
    logger.setLevel(logging.INFO)
    hhru_app_token = dotenv.load_dotenv('HHRU_APP_TOKEN')

if __name__=="__main__":
    main()