import requests
import json


class GithubClient:

    API_BASE_URL = 'https://api.github.com'

    @classmethod
    def get_repos_by_user(cls, user):
        url = f'{cls.API_BASE_URL}/users/{user}/repos'
        response = requests.get(url)
        if response.status_code == 200:
            # todo: verificar todos os dados que tenho de retorno
            return {'status_code': 200, 'body': response.json()}
        else:
            return {'status_code': response.status_code, 'body': f'Error: Erro na requisição {url}'}
