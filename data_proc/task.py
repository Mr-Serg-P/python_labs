import random
from time import sleep

class Task:

    def __init__(self, task_id):
        self._id = task_id
        self._work_time = random.randint(1, 10)

    def __call__(self, *args, **kwargs):
        sleep(self._work_time)

    def __repr__(self):
        return str(self._id)
