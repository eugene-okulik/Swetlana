import requests


def get_all_objects():
    response = requests.get('http://167.172.172.115:52353/object')
    return response.json()


def create_obj():
    body = {
        "data": {"apple": 2, "orange": 3},
        "name": "I'm a new post"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post('http://167.172.172.115:52353/object',
        json=body,
        headers=headers
        )
    return response.json()["id"]


def clear(post_id):
    requests.delete(f'http://167.172.172.115:52353/object/{post_id}')


def put_object():
    post_id = create_obj()
    body = {
        "data": {"apple": 2, "peach": 4},
        "name": "I'm an old post"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(f'http://167.172.172.115:52353/object/{post_id}',
        json=body,
        headers=headers
        ).json()
    assert response['name'] == "I'm an old post"
    clear(post_id)


def patch_obj():
    post_id = create_obj()
    body = {
        'data': {"banana": 1}
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(f'http://167.172.172.115:52353/object/{post_id}',
        json=body,
        headers=headers
        ).json()
    assert response['data'] == {"banana": 1}
    clear(post_id)


put_object()
patch_obj()
print(get_all_objects())
