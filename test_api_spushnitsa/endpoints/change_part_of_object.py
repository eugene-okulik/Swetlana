from test_api_spushnitsa.endpoints.endpoint import EndpointMain
import allure
import requests


class ChangePartOfObject(EndpointMain):

    @allure.step('change only one element of object')
    def update_object_part(self, post_id, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.patch(
            f'{self.url}/{post_id}',
            json=payload,
            headers=headers
        )
        self.json = self.response.json()
        return self.response
