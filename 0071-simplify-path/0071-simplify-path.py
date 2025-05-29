class Solution:
    def simplifyPath(self, path: str) -> str:
        cur = "";
        mystack=[];
        for ch in path + "/":
            if ch=="/":
                if cur=="..":
                    if mystack: mystack.pop();
                elif cur!="" and cur!=".":
                    mystack.append(cur);
                cur= "";
            else:
                cur= cur+ch;
        return "/"+"/".join(mystack);

             