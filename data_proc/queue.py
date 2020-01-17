

class Queue:

    def __init__(self):
        self._data = []

    def append(self, data):
        self._data.append(data)

    def pop(self):
        return self._data.pop(0)

    def has_data(self):
        return True if len(self._data) else False
