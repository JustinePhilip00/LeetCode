class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s):1};

        def dfs(i):
            if i in dp:
                return dp[i];
            if s[i]=="0":
                return 0;

            res = dfs(i+1);
            if (i+1 < len(s) and (s[i]=="1" or
            s[i]=="2" and s[i+1] in "0123456")):
                res= res+dfs(i+2);

            dp[i] = res;
            return res;
        return dfs(0);
# class Solution:
#     def numDecodings(self, s: str) -> int:
#         num =0;
#         dp = [0]*(len(s)+1);
#         dp[len(s)]=1;
#         if not s or s[0]=="0":
#             return 0;
#         for i in range(len(s)-1,-1,-1):
#             if s[i]!="0":
#                 dp[i]= dp[i+1];
#             if i+1<len(s) and (s[i]=="1" or (s[i]=="2" and s[i+1] in "0123456" )):
#                 dp[i]=dp[i]+dp[i+2];
#         return dp[0];
        



         
        