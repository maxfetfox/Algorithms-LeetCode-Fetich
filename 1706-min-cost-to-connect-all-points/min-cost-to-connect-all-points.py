class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        length = len(points)
        used_points = [False] * length # используется для того, чтобы не трогать использованные точки
        min_distance = [float('inf')] * length # длина рёбер

        min_distance[0] = 0

        for _ in points:
            current_minimum = -1
            for i in range(length): # ищется точка. если у неё минимальное расстояние среди всех нерассмотренных точек,
                                    # то ребро становится "закреплённым"
                if not used_points[i] and (current_minimum == -1 or min_distance[i] < min_distance[current_minimum]):
                    current_minimum = i

            used_points[current_minimum] = True
            
            # цикл отвечает за выбор точек, с которыми можно соединить текуще-минимальную точку. если расстояние действительно стало эффективнее – образуется новая связь
            for i in range(length):
                if not used_points[i]:
                    distance = abs(points[current_minimum][0] - points[i][0]) + abs(points[current_minimum][1] - points[i][1])
                    if distance < min_distance[i]:
                        min_distance[i] = distance

        return sum(min_distance)