from collections import deque


class BufferFullException(Exception):
    pass


class BufferEmptyException(Exception):
    pass


class CircularBuffer(object):
    def __init__(self, capacity):
        self.clear()
        self.capacity = capacity

    def read(self):
        if len(self.buffer) <= 0:
            raise BufferEmptyException("Empty")
        return self.buffer.popleft()

    def write(self, data):
        if len(self.buffer) >= self.capacity:
            raise BufferFullException("Full")
        self.buffer.append(data)

    def overwrite(self, data):
        if len(self.buffer) >= self.capacity:
            self.buffer.rotate(-1)
            self.buffer[-1] = data
        else:
            self.write(data)

    def clear(self):
        self.buffer = deque()
