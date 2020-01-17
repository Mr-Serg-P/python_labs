from threading import Thread
from random import randint, choice
from time import sleep

from processor import Processor
from queue import Queue
from stack import Stack
from task import Task


class Scheduler:

    def __init__(self, ids: int=3):
        self._pool = {}
        for processor_id in range(ids):
            self._pool[processor_id] = Processor(processor_id)
        self._stack = Stack()
        self._queue = Queue()
        self._task_generator = Thread(target=self._generate_task)
        self._schedule_thread = Thread(target=self._schedule)
        self._is_running = True
        self._cur_task_id = 0

    def _generate_task(self):
        while self._is_running:
            task = Task(self._cur_task_id)
            self._cur_task_id += 1
            processor_id = choice(tuple(self._pool.keys()))
            self._queue.append((processor_id, task,))
            print("Task {} generated for {}".format(repr(task), processor_id))
            sleep(randint(0, 5))

    def _schedule(self):
        while self._is_running:
            if self._stack.has_data():
                processor_id, task = self._stack.pop()
                print("Task {} popped from stack for processor {}".format(repr(task), processor_id))
            elif self._queue.has_data():
                processor_id, task = self._queue.pop()
                print("Task {} popped from queue for processor {}".format(repr(task), processor_id))

            if self._pool[processor_id].is_running():
                print("Task {} for processor {} pushed to stack".format(repr(task), processor_id))
                self._stack.push((processor_id, task))
            else:
                self._pool[processor_id](task)

            sleep(1)

    def run(self):
        for _, processor in self._pool.items():
            processor.start()

        self._task_generator.start()
        self._schedule_thread.start()

    def stop(self):
        self._is_running = False

        for _, processor in self._pool.items():
            processor.stop()

        if self._task_generator.is_alive():
            self._task_generator.join()
        if self._schedule_thread.is_alive():
            self._schedule_thread.join()
