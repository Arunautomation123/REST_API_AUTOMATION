from locust import User, task, constant


class MyScript(User):
    wait_time = constant(1)
    weight = 1

    @task
    def launch(self):
        print("Launching the browser")

    @task
    def search(self):
        print("Searching")


class MyScript2(User):
    wait_time = constant(1)
    weight = 2

    @task
    def launch2(self):
        print("Launching the browser2")

    @task
    def search2(self):
        print("Searching2")