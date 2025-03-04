from test_api_spushnitsa.endpoints.endpoint import EndpointMain
import allure
import requests


class UpdatePost(EndpointMain):

    @allure.step('change all payload')
    def put_post(self, post_id, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.put(
            f'{self.url}/{post_id}',
            json=payload,
            headers=headers
        )
        self.json = self.response.json()
        return self.response
