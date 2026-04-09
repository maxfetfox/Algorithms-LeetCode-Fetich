class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        distances = [float('inf')] * (n + 1) # для удобства в обоих списках счёт начинается с 1
        parents = [None] * (n + 1)

        distances[k] = 0

        for _ in range(n - 1): # уменьшение расстояния
            for u, v, w in times:
                if distances[u] != float('inf') and distances[v] > distances[u] + w:
                    distances[v] = distances[u] + w
                    parents[v] = u

        for u, v, w in times: # если получится так, что расстояние можно ещё уменьшать после всех проходов,
                              # то это бесконечный цикл и решения нет
            if distances[v] > distances[u] + w:
                return -1

        time = max(distances[1:]) # так как отсчёт начинается с 1, то элемент 0 всегда inf
        return time if time != float('inf') else -1