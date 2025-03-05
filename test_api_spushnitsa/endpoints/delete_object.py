from test_api_spushnitsa.endpoints.endpoint import EndpointMain
import requests
import allure


class DeleteObject(EndpointMain):

    @allure.step('delete one object')
    def delete_object(self, object_id):
        self.response = requests.delete(f'{self.url}/{object_id}')
        return self.response

    @allure.step('check status code is 404')
    def check_status_code_is_404(self, object_id):
        self.response = requests.get(f'{self.url}/{object_id}')
        assert self.response.status_code == 404
