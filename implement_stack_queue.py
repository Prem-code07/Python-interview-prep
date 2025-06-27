from collections import deque

class StackUsingQueues:
    def __init__(self):
        self.q = deque()

    def push(self, x):
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self):
        return self.q.popleft() if self.q else None

    def top(self):
        return self.q[0] if self.q else None

    def empty(self):
        return len(self.q) == 0
