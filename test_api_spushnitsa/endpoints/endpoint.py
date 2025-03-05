import allure


class EndpointMain:
    url = 'http://167.172.172.115:52353/object'
    response = None
    json = None
    headers = {'Content-Type': 'application/json'}
    object_id = None

    @allure.step('Check status code is 200')
    def check_response_code_is_200(self):
        assert self.response.status_code == 200

    @allure.step('Check post name')
    def check_object_name(self, name):
        assert self.json['name'] == name

    @allure.step('Check collection of objects is created')
    def check_data_content(self, data):
        assert self.json['data'] == data
