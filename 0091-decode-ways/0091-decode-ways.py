# class Solution:
#     def numDecodings(self, s: str) -> int:
#         dp = [1]*(len(s)+1);
#         for i in range(len(s)-1,-1,-1):
#             if s[i]=="0":
#                 dp[i]=0;
#             else:
#                 dp[i]=dp[i+1];
#             if i+1 <len(s) and (s[i]=="1"or s[i]=="2" and s[i+1] in "0123456"):
#                 dp[i]=dp[i]+dp[i+2];
#         return dp[0];
class Solution:
    def numDecodings(self, s: str) -> int:
        num =0;
        dp = [0]*(len(s)+1);
        dp[len(s)]=1;
        if not s or s[0]=="0":
            return 0;
        for i in range(len(s)-1,-1,-1):
            if s[i]!="0":
                dp[i]= dp[i+1];
            if i+1<len(s) and (s[i]=="1" or (s[i]=="2" and s[i+1] in "0123456" )):
                dp[i]=dp[i]+dp[i+2];
        return dp[0];
        



         
        