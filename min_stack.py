class MinStack:
    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, x):
        self.stack.append(x)
        if not self.min or x <= self.min[-1]:
            self.min.append(x)

    def pop(self):
        if self.stack:
            if self.stack[-1] == self.min[-1]:
                self.min.pop()
            return self.stack.pop()

    def getMin(self):
        if self.min:
            return self.min[-1]
s = MinStack()
s.push(5)
s.push(2)
s.push(4)
print(s.getMin())
s.pop()
print(s.getMin())
s.pop()
print(s.getMin()) 
