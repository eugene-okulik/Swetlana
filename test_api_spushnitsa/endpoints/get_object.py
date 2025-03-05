import requests
from test_api_spushnitsa.endpoints.endpoint import EndpointMain
import allure


class GetObjects(EndpointMain):

    @allure.step('get all objects')
    def get_objects(self):
        self.response = requests.get(self.url)
        assert type(self.response.json()) == dict
