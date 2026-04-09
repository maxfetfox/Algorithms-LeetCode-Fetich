class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        distances = [float('inf')] * (n + 1)
        parents = [None] * (n + 1)

        distances[k] = 0

        for _ in range(n - 1):
            for u, v, w in times:
                if distances[u] != float('inf') and distances[v] > distances[u] + w:
                    distances[v] = distances[u] + w
                    parents[v] = u

        for u, v, w in times:
            if distances[u] != float('inf') and distances[v] > distances[u] + w:
                return -1

        time = max(distances[1:])
        return time if time != float('inf') else -1