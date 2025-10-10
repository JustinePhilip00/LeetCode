class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        mylist=[];
        start = 0;
        end = len(p)-1;
        p = sorted(p);
        while end<len(s):
            if sorted(s[start: end+1]) == p:
                mylist.append(start);
            start = start +1;
            end = end +1;
        return mylist;

            

            