import logging
import os

import requests

from dotenv import load_dotenv

LANGS = (
    'JavaScript',
    'Java',
    'Python',
    'Ruby',
    'PHP',
    'C++',
    'C#',
    'C',
    'Go',
)

logger = logging.getLogger(__name__)

def get_hhru_token(hhru_client_id, hhru_client_secret):
    url = 'https://hh.ru/oauth/token'
    data = {
        'grant_type': 'client_credentials',
        'client_id': hhru_client_id,
        'client_secret': hhru_client_secret,
    }
    resp = requests.post(url, data=data)
    resp.raise_for_status()
    hhru_resp = resp.json()
    print(hhru_resp['access_token'])
    print(hhru_resp['token_type'])

def get_hhru_vacancies(access_token: str, profession: str, area: int, period: int) -> dict:
    params = {
        'text': profession,
        'area': str(area),
        'period': str(period)
    }
    header = {'Authorization': f'Bearer {access_token}'}
    url = 'https://api.hh.ru/vacancies'
    resp = requests.get(url, params=params, headers=header)
    resp.raise_for_status()
    return resp.json()

def main():
    logger.setLevel(logging.INFO)
    load_dotenv()
    hhru_client_id = os.getenv('HHRU_CLIENT_ID')
    hhru_client_secret = os.getenv('HHRU_CLIENT_SECRET')
    hhru_access_token = os.getenv('HHRU_ACCESS_TOKEN')
    vacancies = get_hhru_vacancies(hhru_access_token, 'программист', 1, 30)

if __name__=="__main__":
    main()