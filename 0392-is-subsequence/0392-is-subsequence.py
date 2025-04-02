class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l1=0;
        l2=0;
        if not s:
            return True;
        for l2 in range(len(t)):
            if l1<len(s) and t[l2] == s[l1]:
                l1= l1+1;
        return True if l1 == len(s) else False;