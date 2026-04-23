class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        # отмечаем каждую сумму недостижимой конечным числом монет
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        if amount == 0:
            return 0

        # отмечаем каждую сумму, которую можно достигнуть одной монетой как 1
        for coin in coins:
            # проверка, чтобы индекс не выходил за пределы списка
            if coin <= amount:
                dp[coin] = 1

        # начинаем счёт с 1
        for i in range(1, len(dp)):
            for coin in coins:
                # проверка, чтобы индекс не ломался
                if i >= coin:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
                    # где i – текущий элемент, а i – coin – элемент, к которому если прибавить coin, получится элемент
                    # с индексом i. + 1 к нему нужен, так как у i становится на одну монету больше, чтобы достигнуть его
                    # сумму. min() выбирает более выгодный вариант
        return dp[amount] if dp[amount] != float('inf') else -1