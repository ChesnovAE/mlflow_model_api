import requests


class ModelApi:
    def __init__(self,
                 host: str,
                 port: str,
                 is_http: bool = True) -> None:
        if is_http:
            self._proto = 'http'
        else:
            self._proto = 'https'
        self._host = host
        self._port = port
        self._base_url = f'{self._proto}://{self._host}:{self._port}/api/2.0/mlflow/'
    
    def get_model_by_name(self, model_name: str):
        params = {
            'name': model_name
        }
        suffix = 'registered-models/get'
        response = requests.get(self._base_url + suffix, params=params).json()
        return response