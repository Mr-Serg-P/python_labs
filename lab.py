from task import Task


class Lab:
    
    def __init__(self, number, *tasks):
        self.number = int(number)
        self.tasks = [Task(i) for i in range(len(tasks))]

    def __call__(self):
        self.__str__()

    def __str__(self):
        return '%s\n%s\n%s\n' % ('-' * 15 + ' Lab %i ' % self.number + '-' * 15, ''.join(['\n\t%s' % task() for task in self.tasks]), '-' * 45 + '\n')
