from threading import Thread


class Processor:

    def __init__(self, processor_id):
        self._processor_id = processor_id
        self._thread = Thread(target=self._run)
        self._task = None
        self._is_running = True

    def _run(self):
        while self._is_running:
            if self._task:
                print("Processor {} started to execute task {}".format(self._processor_id, repr(self._task)))
                self._task()
                print("Processor {} finished to execute task {}".format(self._processor_id, repr(self._task)))
                self._task = None

    def is_running(self):
        return True if self._task else False

    def __call__(self, task):
        self._task = task

    def start(self):
        self._thread.start()

    def stop(self):
        self._is_running = False
        self._thread.join()

