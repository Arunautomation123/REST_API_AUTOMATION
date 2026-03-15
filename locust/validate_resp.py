from locust import task, SequentialTaskSet, HttpUser, TaskSet, constant, tag

class MyUser(SequentialTaskSet):
    def on_start(self):
        print("on_start")


    @tag('get')
    @task
    def task_1(self):
        expected_resp = ''
        with self.client.get("/json", catch_response = True, name="JSON") as response:
            result = True if expected_resp in response.text else False
            print(self.task_1.__name__, result)
            response.success()

    @tag('post')
    @task
    def task_2(self):
        expected_resp = '*'
        result = 'Fail'
        with self.client.get("/json", catch_response = True, name="JSON") as response:
            result = True if expected_resp in response.text else False
            print(self.task_1.__name__, result)
            response.failure("Got error")


    def on_stop(self):
        print("on_stop")


class MyHttpUser(HttpUser):
    host = "https://httpbin.org"
    wait_time = constant(1)
    tasks = [MyUser]