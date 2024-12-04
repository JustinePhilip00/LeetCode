class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        mod = 10**9 + 7
        dp = [0] * (len(pressedKeys) + 1)
        dp[len(pressedKeys)] = 1  # Base case: 1 way to decode empty
        
        max_press = {
            '2': 3, '3': 3, '4': 3, '5': 3, '6': 3, '8': 3,
            '7': 4, '9': 4
        }

        for i in range(len(pressedKeys) - 1, -1, -1):
            dp[i] = dp[i + 1]  # Single press
            for j in range(2, max_press[pressedKeys[i]] + 1):
                if i + j <= len(pressedKeys) and pressedKeys[i:i + j] == pressedKeys[i] * j:
                    dp[i] = (dp[i] + dp[i + j]) % mod

        return dp[0]
