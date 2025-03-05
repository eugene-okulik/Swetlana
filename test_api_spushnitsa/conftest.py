import pytest
from test_api_spushnitsa.endpoints.create_object import CreateObject
from test_api_spushnitsa.endpoints.get_object import GetObjects
from test_api_spushnitsa.endpoints.change_object import ChangeObject
from test_api_spushnitsa.endpoints.delete_object import DeleteObject
from test_api_spushnitsa.endpoints.change_part_of_object import ChangePartOfObject


DATA_CREATE_OBJECT = {"data": {"apple": 2, "peach": 4}, "name": "I'm an old post"}


@pytest.fixture()
def create_object_endpoint():
    return CreateObject()


@pytest.fixture()
def get_objects_endpoint():
    return GetObjects()


@pytest.fixture()
def update_object_endpoint():
    return ChangeObject()


@pytest.fixture()
def get_object_id(create_object_endpoint):
    create_object_endpoint.new_object(DATA_CREATE_OBJECT)
    yield create_object_endpoint.object_id


@pytest.fixture()
def create_object_id_then_delete_it(delete_object_endpoint, create_object_endpoint):
    create_object_endpoint.new_object(DATA_CREATE_OBJECT)
    yield create_object_endpoint.object_id
    delete_object_endpoint.delete_object(create_object_id_then_delete_it)


@pytest.fixture()
def update_part_of_object_endpoint():
    return ChangePartOfObject()


@pytest.fixture()
def delete_object_endpoint():
    return DeleteObject()
