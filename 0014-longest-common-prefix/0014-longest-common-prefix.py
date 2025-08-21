class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = "";
        itr = min(len(s) for s in strs);
        for i in range(itr):
            for s in strs:
                if s[i]!=strs[0][i]:
                    return res;
            res = res + strs[0][i];
        return res;