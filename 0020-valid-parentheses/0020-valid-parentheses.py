class Solution:
    def isValid(self, s: str) -> bool:
        # mymap = { ")":"(", "}":"{","]":"["};
        # mylist = list();
        # for ch in s:
        #     if ch not in mymap:
        #         mylist.append(ch);
        #         continue;
        #     if not mylist or mymap[ch]!=mylist[-1]:
        #         return False;
        #     mylist.pop();
        # return not mylist;

        mystack = [];
        if len(s) ==1:
            return False;
        for c in s:
            if c in "[,(,{":
                mystack.append(c);
            if c == "]": 
                if not mystack or mystack[len(mystack)-1] != "[":
                    return False;
                mystack.pop();
            elif c== ")": 
                if not mystack or mystack[len(mystack)-1]!= "(":
                    return False
                mystack.pop();
            elif c== "}":
                if not mystack or mystack[len(mystack)-1]!="{":
                    return False;
                mystack.pop();
            # else:
            #     return False;
        return True if len(mystack) == 0 else False;
                
                
                
        