
class Task:
    result = None

    def __init__(self, task_number):
        self.number = int(task_number)


    # def data_input(self):
    #     raise NotImplementedError

    # def solve(self, *args, **kwargs):
    #     raise NotImplementedError

    # def __call__(self):
    #     self.data_input()


    def __str__(self):
        return 'task %i' % self.number


