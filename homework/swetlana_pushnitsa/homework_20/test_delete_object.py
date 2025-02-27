import requests
import allure


@allure.epic('API test delete')
@allure.feature('Block feature')
@allure.severity('blocker')
@allure.story('Delete one object')
def test_delete_object(create_obj, before_after):
    with allure.step(f'Delete the creating object with id {create_obj}'):
        response_delete = requests.delete(f'http://167.172.172.115:52353/object/{create_obj}')
    with allure.step('Return the status code'):
        assert response_delete.status_code == 200
    with allure.step(f'Get the post with deleting id {create_obj}'):
        response_get_after = requests.get(f'http://167.172.172.115:52353/object/{create_obj}')
    with allure.step('Return status code, to show that object is not found'):
        assert response_get_after.status_code == 404
