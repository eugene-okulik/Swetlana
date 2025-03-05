import allure
import requests
from test_api_spushnitsa.endpoints.endpoint import EndpointMain


class CreateObject(EndpointMain):

    @allure.step('create a new object')
    def new_object(self, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(
            self.url,
            json=payload,
            headers=headers
        )
        self.json = self.response.json()
        self.object_id = self.json['id']
        return self.response
