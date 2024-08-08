class Solution {
    public String removeStars(String s) {
       Stack<Character> stack = new Stack<>();
        for(int i=0;i<s.length();i++)
        {
            stack.push(s.charAt(i));
            if(s.charAt(i)=='*')
            {
                stack.pop();
                stack.pop();
            }
        }
        StringBuilder output= new StringBuilder();
        for(char c: stack)
        {
            output.append(c);
        }
        return output.toString();
    }
}