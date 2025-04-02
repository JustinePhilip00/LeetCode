class Solution {
    public boolean isSubsequence(String s, String t) {
        int l1=0;
        if(s.length() == 0){
            return true;
        }
        for (int l2=0; l2<t.length(); l2++){
            if (l1<s.length() && t.charAt(l2) == s.charAt(l1)){
                l1=l1+1;
            }
        }
        if(l1==s.length()){
            return true;
        }
        return false;
    }
}