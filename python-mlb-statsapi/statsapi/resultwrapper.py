import requests
import logging

from typing import Dict, List
from .exceptions import MlbStatsApiException


class APIResult:
    def __init__(self, status_code: int, message: str, data: Dict = {}):
        self.status_code = int(status_code)
        self.message = str(message)

        self.data = data
        if 'copyright' in data:
            del data['copyright']


class APIHelper:
    def __init__(self, host: str = 'statsapi.mlb.com', version: str = 'v1', logger: logging.Logger = None):
        self.url = f"https://{host}/api/{version}/"
        self._logger = logger or logging.getLogger(__name__)
        self._logger.setLevel(logging.DEBUG)

    def _keys_to_lower(self, data) -> dict:
        if isinstance(data, Dict):
            new_dict = {}
            for k, v in data.items():
                new_dict[k.lower()] = self._keys_to_lower(v)
            return new_dict
        
        elif isinstance(data, List):
            new_list = []
            for i in data:
                new_list.append(self._keys_to_lower(i))
            return new_list
        
        else:
            return data
        
    def get(self, endpoint: str, ep_params: Dict = None, data: Dict = None) -> APIResult:

        full_url = self.url + endpoint
        #print(full_url)
        log_pre = f"url={full_url}"
        log_post = " ,".join((log_pre, 'success={}, status_code={}, message={}, url={}'))

        try:
            self._logger.debug(log_post)
            response = requests.get(url=full_url, params=ep_params)

        except requests.exceptions.RequestException as e:
            self._logger.error(msg=(str(e)))
            raise MlbStatsApiException("NB1 Request Failed") from e
        
        try:
            data = response.json()
        
        except (ValueError, requests.JSONDecodeError) as e:
            self._logger.error(msg=(str(e)))
            raise MlbStatsApiException("NB2 Bad JSON in response") from e
        
        if 200 <= response.status_code <= 299:
            self._logger.debug(msg=log_post.format('success',
            response.status_code, response.reason, response.url))

            data = self._keys_to_lower(data)
            return APIResult(response.status_code, message=response.reason, data=data)
        
        elif 400 <= response.status_code <= 499:
            self._logger.error(msg=log_post.format('Invalid Request',
            response.status_code, response.reason, response.url))

            return APIResult(response.status_code, message=response.reason, data={})
        
        elif 500 <= response.status_code <= 599:
            self._logger.error(msg=log_post.format('Internal error occurred', 
            response.status_code, response.reason, response.url))

            raise MlbStatsApiException(f"{response.status_code}: {response.reason}")
        
        else:
            raise MlbStatsApiException(f"{response.status_code}: {response.reason}")