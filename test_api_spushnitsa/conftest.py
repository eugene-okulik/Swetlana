import pytest
from test_api_spushnitsa.endpoints.create_post import CreatePost
from test_api_spushnitsa.endpoints.get_object import GetAllObjects
from test_api_spushnitsa.endpoints.change_post import UpdatePost
from test_api_spushnitsa.endpoints.delete_post import DeletePost
from test_api_spushnitsa.endpoints.patch_post import PatchPost


DATA_CREATE_OBJECT = {"data": {"apple": 2, "peach": 4}, "name": "I'm an old post"}


@pytest.fixture()
def create_post_endpoint():
    return CreatePost()


@pytest.fixture()
def get_post_endpoint():
    return GetAllObjects()


@pytest.fixture()
def put_post_endpoint():
    return UpdatePost()


@pytest.fixture()
def post_id(create_post_endpoint):
    create_post_endpoint.new_post(DATA_CREATE_OBJECT)
    yield create_post_endpoint.post_id


@pytest.fixture()
def patch_post_endpoint():
    return PatchPost()


@pytest.fixture()
def delete_post_endpoint():
    return DeletePost()
