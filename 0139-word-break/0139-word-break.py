class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True  # An empty string can always be segmented (base case)

        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break  # No need to check further for this i

        return dp[len(s)]  # This will be True if the whole string can be segmented