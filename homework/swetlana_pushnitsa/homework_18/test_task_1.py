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

    def test_get_all_objects(self, start_end, before_after):
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
    def test_patch_obj(self, create_del_obj, before_after):
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


class TestApiCreateDeleteObj:

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
    def create_obj(self, request):
        body = {
            "data": request.param,
            "name": "I'm a new post"
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.post(
            'http://167.172.172.115:52353/object',
            json=body,
            headers=headers
        ).json()
        return response['data']

    @pytest.mark.parametrize("data", [{"cherry": 5, "melon": 3}, {}, {"tomato": "six"}])
    def test_delete_obj(self, data, before_after):
        requests.delete(f'http://167.172.172.115:52353/object/{data}')
