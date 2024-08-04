class Solution {
    public int lengthOfLongestSubstring(String s) {
      Set <Character> hashset = new HashSet<Character> ();
      int i=0;
      int j=0;
      int maxLength=0;
      while(j<s.length())
      {
          if(!hashset.contains(s.charAt(j)))
          {
              hashset.add(s.charAt(j));
              // index=s.charAt(i);
              j++;
              maxLength=Math.max(maxLength,j-i);
              System.out.println(hashset);
              
          }
          else
          {
              hashset.remove(s.charAt(i));
              i++;
              
          }
       }
      
        return maxLength;
          
      
    }
}