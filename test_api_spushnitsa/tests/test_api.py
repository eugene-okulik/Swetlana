import pytest
import allure


TEST_DATA = [{"data": {"cherry": 5, "melon": 3}, "name": "I'm new post"},
             {"data": {}, "name": "I'm new post"},
             {"data": {"tomato": "six"}, "name": "I'm new post"}]

@allure.feature('create_objects')
@pytest.mark.parametrize("data", TEST_DATA)
def test_create_object(create_post_endpoint, data):
    create_post_endpoint.new_post(payload=data)
    create_post_endpoint.check_response_code()
    create_post_endpoint.check_data_content(data['data'])


@allure.feature('get all objects from API')
@allure.severity('minor')
def test_get_all_objects(get_post_endpoint):
    get_post_endpoint.get_objects()


@allure.feature('put object')
def test_update_post(post_id, put_post_endpoint, delete_post_endpoint):
    payload = {"data": {"apple": 2, "peach": 4}, "name": "I'm an old post"}
    put_post_endpoint.put_post(post_id, payload)
    put_post_endpoint.check_response_code()
    put_post_endpoint.check_post_name(payload['name'])
    delete_post_endpoint.delete_object(post_id)


@allure.feature('patch object')
def test_patch_post(post_id, patch_post_endpoint, delete_post_endpoint):
    payload = {'data': {"banana": 1}}
    patch_post_endpoint.patch_post(post_id, payload)
    patch_post_endpoint.check_response_code()
    patch_post_endpoint.check_data_content(payload['data'])
    delete_post_endpoint.delete_object(post_id)


@allure.feature('delete object')
def test_delete_post(create_post_endpoint, post_id, delete_post_endpoint):
    payload = {"data": {"apple": 2, "peach": 4}, "name": "I'm an old post"}
    create_post_endpoint.new_post(payload)
    post_id = create_post_endpoint.post_id
    create_post_endpoint.check_data_content(payload['data'])
    create_post_endpoint.check_response_code()
    delete_post_endpoint.delete_object(post_id)
    delete_post_endpoint.check_response_code()
