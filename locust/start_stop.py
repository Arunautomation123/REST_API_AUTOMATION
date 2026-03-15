from locust import task, User, constant

class MyUser(User):
    wait_time = constant(1)

    def on_start(self):
        print("Starting")

    @task
    def task_1(self):
        print("Task1 running ")

    def on_stop(self):
        print("Stopping")