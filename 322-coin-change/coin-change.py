class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        if amount == 0:
            return 0

        for coin in coins:
            if coin <= amount:
                dp[coin] = 1

        for i in range(1, len(dp)):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1



obj = Solution()
print(obj.coinChange([1], 0))