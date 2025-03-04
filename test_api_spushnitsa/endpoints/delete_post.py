from test_api_spushnitsa.endpoints.endpoint import EndpointMain
import requests
import allure


class DeletePost(EndpointMain):
    @allure.feature('Block feature')
    @allure.severity('blocker')
    @allure.story('Test delete object')
    @allure.step('delete one object')
    def delete_object(self, post_id):
        self.response = requests.delete(f'{self.url}/{post_id}')
        return self.response
