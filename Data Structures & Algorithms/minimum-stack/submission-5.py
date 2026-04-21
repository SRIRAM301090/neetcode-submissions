class MinStack:

    def __init__(self):
        self.stack = []
        self.minval = []
        self.minimum = float('inf') 

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minimum = min(val, self.minimum)
        self.minval.append(self.minimum)

    def pop(self) -> None:
        self.stack.pop()
        self.minval.pop()
        self.minimum = self.minval[-1] if self.minval else float('inf')

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minval[-1]
