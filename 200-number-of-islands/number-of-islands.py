class MyQueue:
    def __init__(self):
        self.in_stack = [] # элементы добавляются сюда при push
        self.out_stack = [] # сюда добавляются элементы из in_stack в обратном порядке и последний элемент используется для возвращения в pop

    def push(self, x) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        if len(self.out_stack) == 0: # элементы добавляются только в том случае, если out_stack пуст. иначе просто возвращается первый элемент. это существенно ускоряет работу
            for _ in range(len(self.in_stack)):
                self.out_stack.append(self.in_stack.pop())
            return self.out_stack.pop()
        return self.out_stack.pop()

    def peek(self) -> int:
        if len(self.in_stack) == 0 or len(self.out_stack) > 0: # пренебрегаем случаем если оба стека пусты
            return self.out_stack[-1]
        return self.in_stack[0]

    def empty(self) -> bool:
        if len(self.in_stack) == 0 and len(self.out_stack) == 0:
            return True
        return False


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        size_m = len(grid)
        size_n = len(grid[0])
        count = 0

        queue = MyQueue()

        for i in range(size_m):
            for j in range(size_n):
                if grid[i][j] == '1':
                    count += 1
                    queue.push((i, j))
                    grid[i][j] = '0'
                    while not queue.empty():
                        current_item = queue.pop()

                        row = current_item[0]
                        col = current_item[1]

                        if 0 <= row - 1 < size_m:
                            if grid[row - 1][col] == '1':
                                grid[row - 1][col] = '0'
                                queue.push((row - 1, col))
                        if 0 <= row + 1 < size_m:
                            if grid[row + 1][col] == '1':
                                grid[row + 1][col] = '0'
                                queue.push((row + 1, col))
                        if 0 <= col - 1 < size_n:
                            if grid[row][col - 1] == '1':
                                grid[row][col - 1] = '0'
                                queue.push((row, col - 1))
                        if 0 <= col + 1 < size_n:
                            if grid[row][col + 1] == '1':
                                grid[row][col + 1] = '0'
                                queue.push((row, col + 1))
        return count