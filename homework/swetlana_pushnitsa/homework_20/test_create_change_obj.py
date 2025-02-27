import pytest
import requests
import allure


@allure.epic('API test create')
@allure.feature('Essential features')
class TestCreateObj:

    @allure.story('Create a three new objects')
    @pytest.mark.parametrize("data", [{"cherry": 5, "melon": 3}, {}, {"tomato": "six"}])
    def test_create_object(self, data, before_after, start_end):
        with allure.step('Create 3 objects in every iteration'):
            body = {
                "data": data,
                "name": "I'm a new post"
            }
            headers = {'Content-Type': 'application/json'}
            response = requests.post(
                'http://167.172.172.115:52353/object',
                json=body,
                headers=headers
            )
        with allure.step('Check status code'):
            assert response.status_code == 200
        with allure.step('Check collection of objects is created'):
            assert response.json()['data'] == data

    @allure.severity('trivial')
    @allure.description('Test checks that collection of objects is dict')
    @allure.story('Get all objects')
    def test_get_all_objects(self, before_after):
        response = requests.get('http://167.172.172.115:52353/object')
        assert type(response.json()) == dict

    @allure.story('Change all info for one object')
    @allure.tag('Test with apple')
    @pytest.mark.critical
    def test_put_object(self, create_del_obj, before_after):
        body = {
            "data": {"apple": 2, "peach": 4},
            "name": "I'm an old post"
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.put(
            f'http://167.172.172.115:52353/object/{create_del_obj}',
            json=body,
            headers=headers
        ).json()
        assert response['name'] == "I'm an old post"

    @allure.severity('minor')
    @allure.id(54)
    @allure.story('Change part of one object')
    @pytest.mark.medium
    def test_patch_object(self, create_del_obj, before_after):
        body = {
            'data': {"banana": 1}
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.patch(
            f'http://167.172.172.115:52353/object/{create_del_obj}',
            json=body,
            headers=headers
        ).json()
        assert response['data'] == {"banana": 1}
