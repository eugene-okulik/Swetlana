import faker
from locust import task, HttpUser
import random


class ObjectApi(HttpUser):
    fake = faker.Faker()
    payload = {
        "data": {"name": fake.name(), "age": random.randint(1, 100)},
        "name": fake.user_name()
    }
    headers = {'Content-Type': 'application/json'}

    @task(2)
    def get_all_objects(self):
        self.client.get('/object')

    @task(4)
    def get_one_object(self):
        self.client.get(f'/object/{random.randrange(230, 244)}')

    @task(1)
    def create_new_object(self):
        self.client.post(
            url = '/object',
            json = self.payload,
            headers = self.headers
        )

    @task(2)
    def change_object(self):
        self.client.put(
            url = f'/object/{random.randrange(230, 244)}',
            json = self.payload,
            headers = self.headers
        )

    @task(3)
    def change_data_in_object(self):
        self.client.patch(
            url=f'/object/{random.choice([230, 231, 238])}',
            json = {"data": {"name": self.fake.name(), "age": random.randint(1, 100)}},
            headers = self.headers
        )
