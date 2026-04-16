class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        length = len(points)
        used_points = [False] * length
        min_distance = [float('inf')] * length

        min_distance[0] = 0

        for _ in points:
            current_minimum = -1
            for i in range(length):
                if not used_points[i] and (current_minimum == -1 or min_distance[i] < min_distance[current_minimum]):
                    current_minimum = i

            used_points[current_minimum] = True

            for i in range(length):
                if not used_points[i]:
                    distance = abs(points[current_minimum][0] - points[i][0]) + abs(points[current_minimum][1] - points[i][1])
                    if distance < min_distance[i]:
                        min_distance[i] = distance
        
        return sum(min_distance)