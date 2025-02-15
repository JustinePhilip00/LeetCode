class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        dp = [-1] *len(arr);
        if len(arr) == 1:
            return [-1];
        for i in range (len(arr)-2, -1, -1):
            dp [i] = max(dp[i+1], arr[i+1]);
        return dp;

