import pytest
import allure

TEST_DATA = [{"data": {"cherry": 5, "melon": 3}, "name": "I'm new post"},
             {"data": {}, "name": "I'm new post"},
             {"data": {"tomato": "six"}, "name": "I'm new post"}]


@allure.feature('Create_objects')
@pytest.mark.parametrize("data", TEST_DATA)
def test_create_object(data, create_object_endpoint):
    create_object_endpoint.new_object(payload=data)
    create_object_endpoint.check_response_code_is_200()
    create_object_endpoint.check_data_content(data['data'])


@allure.feature('Get all objects from API')
@allure.severity('minor')
def test_get_objects(get_objects_endpoint):
    get_objects_endpoint.get_objects()


@allure.feature('Update object')
def test_update_object(create_object_id_then_delete_it, update_object_endpoint):
    payload = {"data": {"apple": 2, "peach": 4}, "name": "I'm an old post"}
    update_object_endpoint.update_object(create_object_id_then_delete_it, payload)
    update_object_endpoint.check_response_code_is_200()
    update_object_endpoint.check_object_name(payload['name'])


@allure.feature('Update part of object')
def test_update_part_of_object(create_object_id_then_delete_it, update_part_of_object_endpoint):
    payload = {'data': {"banana": 1}}
    update_part_of_object_endpoint.update_object_part(create_object_id_then_delete_it, payload)
    update_part_of_object_endpoint.check_response_code_is_200()
    update_part_of_object_endpoint.check_data_content(payload['data'])


@allure.feature('Delete object')
@allure.severity('blocker')
def test_delete_object(create_object_endpoint, get_object_id, delete_object_endpoint):
    payload = {"data": {"apple": 2, "peach": 4}, "name": "I'm an old post"}
    create_object_endpoint.new_object(payload)
    delete_object_endpoint.delete_object(get_object_id)
    delete_object_endpoint.check_response_code_is_200()
    delete_object_endpoint.check_status_code_is_404(get_object_id)
