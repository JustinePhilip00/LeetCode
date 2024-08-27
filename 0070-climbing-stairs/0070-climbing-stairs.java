class Solution {
    public int climbStairs(int n) {
        int ptr1=1;
        int ptr2=1;
        for(int i=0;i<n-1;i++)
        {
            int temp = ptr1+ptr2;
            ptr2=ptr1;
            ptr1=temp;
        }
        return ptr1;
    }
}