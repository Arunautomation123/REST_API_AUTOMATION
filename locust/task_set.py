from locust import task, TaskSet, constant, HttpUser, SequentialTaskSet

# class MyTask(TaskSet):
#
#     @task
#     def start_task(self):
#         res = self.client.get('/100')
#         print(res)
#         self.interrupt(reschedule=False)
#
#
#     # @task
#     # class MyAnotherTask(TaskSet):
#     #     @task
#     #     def get_status(self):
#     #         self.client.get('/500')
#     #         print("Status of 500")
#     #         self.interrupt(reschedule=False)
#
# class MyAnotherTask(TaskSet):
#     @task
#     def get_status(self):
#         self.client.get('/500')
#         print("Status of 500")
#         self.interrupt(reschedule=False)
#
# class MyUser(HttpUser):
#     host = 'https://http.cat/'
#     wait_time = constant(1)
#     tasks = [MyTask, MyAnotherTask]

class MySequentialTaskSet(SequentialTaskSet):
    @task
    def get_status(self):
        self.client.get('/500')
        print("Status of 500")

    @task
    def get_status_2(self):
        self.client.get('/200')
        print("Status of 200")

class MyHttpUser(HttpUser):
    host = 'https://http.cat/'
    tasks = [MySequentialTaskSet]
    wait_time = constant(1)