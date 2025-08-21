class Solution:
    def isPalindrome(self, s: str) -> bool:
        # newS =""
        # for ch in s:
        #     if ch.isalnum():
        #         newS = newS+ch.lower();
        # l =0;
        # r= len(newS)-1;
        # while l<=r:
        #     if newS[l]!=newS[r]:
        #         return False;
        #     l=l+1;
        #     r=r-1;
        # return True
        # print(s)
        newS =""
        # print(newS)
        for word in s.split():
            for ch in word:
                if ch.isalnum():
                    newS += ch.lower()
        # print(newS)
        l =0;
        r= len(newS)-1;
        while l<=r:
            if newS[l]!=newS[r]:
                return False;
            l=l+1;
            r=r-1;
        return True

        

            
        
            
        
        
            