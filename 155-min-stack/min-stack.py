class MinStack:
    def __init__(self):
        self.stack = []
        self.mins = [] # для каждого элемента в стеке хранится минимальный элемент на момент его добавления

    def push(self, val: int) -> None:
        if len(self.mins) > 0:
            self.mins.append(min(val, self.mins[-1]))
        else:
            self.mins.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        if len(self.stack) == 0: # ничего не делать
            ...
        else:
            self.stack.pop()
            self.mins.pop()

    def top(self) -> int:
        if len(self.stack) == 0:
            raise Exception("stack is empty")
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins[-1]