import requests
import pytest


@pytest.fixture(scope="session")
def start_end():
    print('\nStart Testing!')
    yield
    print('\nTesting completed')


@pytest.fixture()
def before_after():
    print('\nbefore test')
    yield
    print('\nafter test')


@pytest.fixture()
def create_del_obj():
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
    post_id = response["id"]
    yield post_id
    requests.delete(f'http://167.172.172.115:52353/object/{post_id}')


@pytest.fixture()
def create_obj():
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
    post_id = response["id"]
    return post_id