class Solution:
    def simplifyPath(self, path: str) -> str:
        mystack = [];
        curr = "";
        for ch in path + "/":
            if ch =="/":
                if curr == "..":
                    if mystack: mystack.pop();
                elif curr!="" and curr!=".":
                    mystack.append(curr);
                curr= ""
            
            else:
                curr= curr+ch;

        return "/"+"/".join(mystack);


             