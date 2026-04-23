class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        summ = sum(nums)

        # нет способов собрать нечётную сумму из двух массивов с целыми числами, где суммы двух массивов равны
        if summ % 2 > 0:
            return False

        # создаём список длиной summ // 2, там отмечены суммы, которые можно собрать при помощи существующих чисел.
        # в случае, если последний элемент не будет равен True, то невозможно собрать из существующих чисел две нужные
        # нам полусуммы.
        goal = summ // 2
        dp = [False] * (goal + 1)
        dp[0] = True

        for num in nums:
            for i in range(goal, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]

        return dp[goal]