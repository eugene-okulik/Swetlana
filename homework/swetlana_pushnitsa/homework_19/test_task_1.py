from http.client import responses

import pytest
import requests


class TestApi:

    @pytest.fixture(scope="session")
    def start_end(self):
        print('\nStart Testing!')
        yield
        print('\nTesting completed')

    @pytest.fixture()
    def before_after(self):
        print('\nbefore test')
        yield
        print('\nafter test')

    @pytest.fixture()
    def create_del_obj(self):
        body = {
            "data": {"apple": 2, "orange": 3},
            "name": "I'm a new post"
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.post(
            'http://167.172.172.115:52353/object',
            json=body,
            headers=headers
        ).json()
        self.post_id = response["id"]
        yield self.post_id
        requests.delete(f'http://167.172.172.115:52353/object/{self.post_id}')

    @pytest.fixture()
    def create_obj(self):
        body = {
            "data": {"apple": 2, "orange": 3},
            "name": "I'm a new post"
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.post(
            'http://167.172.172.115:52353/object',
            json=body,
            headers=headers
        ).json()
        self.post_id = response["id"]

    @pytest.mark.parametrize("data", [{"cherry": 5, "melon": 3}, {}, {"tomato": "six"}])
    def test_create_object(self, data, before_after, start_end):
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
        assert response.status_code == 200
        assert response.json()['data'] == data

    def test_get_all_objects(self, before_after):
        response = requests.get('http://167.172.172.115:52353/object')
        assert type(response.json()) == dict

    @pytest.mark.critical
    def test_put_object(self, create_del_obj, before_after):
        body = {
            "data": {"apple": 2, "peach": 4},
            "name": "I'm an old post"
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.put(
            f'http://167.172.172.115:52353/object/{self.post_id}',
            json=body,
            headers=headers
        ).json()
        assert response['name'] == "I'm an old post"

    @pytest.mark.medium
    def test_patch_object(self, create_del_obj, before_after):
        body = {
            'data': {"banana": 1}
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.patch(
            f'http://167.172.172.115:52353/object/{self.post_id}',
            json=body,
            headers=headers
        ).json()
        assert response['data'] == {"banana": 1}

    def test_delete_object(self, create_obj, before_after):
        requests.delete(f'http://167.172.172.115:52353/object/{self.post_id}')
        assert self.post_id not in requests.get('http://167.172.172.115:52353/object/')
