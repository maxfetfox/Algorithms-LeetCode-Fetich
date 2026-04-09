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

    def empty(self) -> bool:
        if len(self.in_stack) == 0 and len(self.out_stack) == 0:
            return True
        return False

    def size(self):
        return len(self.in_stack) + len(self.out_stack)


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        queue = MyQueue()

        m = len(grid)
        n = len(grid[0])

        fresh = 0

        for i in range(m):
            for j in range(n):
                current_element = grid[i][j]
                if current_element == 2:
                    queue.push((i, j))
                elif current_element == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        minutes = 0

        while not queue.empty():
            q_size = queue.size()
            has_rotted = False

            for _ in range(q_size):
                current_item = queue.pop()
                row, col = current_item

                if 0 <= row - 1 < m:
                    if grid[row - 1][col] == 1:
                        grid[row - 1][col] = 2
                        queue.push((row - 1, col))
                        fresh -= 1
                        has_rotted = True
                if 0 <= row + 1 < m:
                    if grid[row + 1][col] == 1:
                        grid[row + 1][col] = 2
                        queue.push((row + 1, col))
                        fresh -= 1
                        has_rotted = True
                if 0 <= col - 1 < n:
                    if grid[row][col - 1] == 1:
                        grid[row][col - 1] = 2
                        queue.push((row, col - 1))
                        fresh -= 1
                        has_rotted = True
                if 0 <= col + 1 < n:
                    if grid[row][col + 1] == 1:
                        grid[row][col + 1] = 2
                        queue.push((row, col + 1))
                        fresh -= 1
                        has_rotted = True
            if has_rotted:
                minutes += 1

        if fresh == 0:
            return minutes
        return -1
