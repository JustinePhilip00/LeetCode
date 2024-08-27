class Solution {
    public boolean isPalindrome(String s) {
        s= s.toLowerCase();
        s= s.replaceAll("[^a-zA-Z0-9]", "");
        
        int ptr1=0;
        int ptr2=s.length()-1;
        while(ptr1<ptr2)
        {
            if(s.charAt(ptr1)!=s.charAt(ptr2))
            {
               
               return false;
            }
            ptr1++;
            ptr2--;
                
        }
        
        return true;
        }
}