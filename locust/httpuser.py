from locust import task, HttpUser, constant

class MyReqRes(HttpUser):
    host = "https://jsonplaceholder.typicode.com/"
    # wait_time = constant(1)

    json_data = {
      "userId": 2,
      "id": 2,
      "title": "sunt aut facere  reprehenderit",
      "body": "quia et suscipit\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
    }

    @task
    def get_users(self):
        self.client.get('posts/1')

    # @task
    # def create_user(self):
    #     self.client.post('posts', json=self.json_data)

