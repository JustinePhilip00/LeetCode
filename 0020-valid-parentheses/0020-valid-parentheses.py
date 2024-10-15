class Solution:
    def isValid(self, s: str) -> bool:
        mymap = { ")":"(", "}":"{","]":"["};
        mylist = list();
        for ch in s:
            if ch not in mymap:
                mylist.append(ch);
                continue;
            if not mylist or mymap[ch]!=mylist[-1]:
                return False;
            mylist.pop();
        return not mylist;
                
                
                
        