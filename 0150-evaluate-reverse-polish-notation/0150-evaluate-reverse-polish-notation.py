class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        mystack = [];
        currResult= 0;
        for token in tokens:
            if token not in "+-/*":
                mystack.append(int(token));
            else:
                a= mystack.pop();
                b = mystack.pop();
                if token == "+":
                    # curr = 0;
                    # popped = mystack.pop()
                    # curr =curr+int(popped);
                    # curr = curr + int(mystack.pop());
                    mystack.append(a+b);
                if token == "-":
                    # curr = 0;
                    # popped = mystack.pop();
                    # curr =curr+int(popped);
                    # curr = curr - int(mystack.pop());
                    mystack.append(b-a);
                if token == "*":
                    # curr = 0;
                    # popped = mystack.pop();
                    # curr = curr * popped;
                    mystack.append(b*a);
                if token == "/":
                    # curr = 0;
                    # popped = mystack.pop();
                    # curr = curr // popped;
                    mystack.append(int(b/a));
        print(mystack)
        return mystack[0];
        