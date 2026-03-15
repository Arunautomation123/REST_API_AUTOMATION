from locust import task, HttpUser, TaskSet, constant, constant_pacing, User, between
import time

class MyUser(User):
    # wait_time = constant(1)
    # wait_time = between(1, 3)
    wait_time = constant_pacing(5)   #task will wait for this time to complete
    @task
    def ping(self):
        time.sleep(6)  # if this delay is greater than constant pacing will not be applied
        print("1 sec delay")