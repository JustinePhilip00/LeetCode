class Solution {
    public int[] productExceptSelf(int[] nums) {
        int leftproduct=1;
        int rightproduct=1;
        int [] leftarray =new int[nums.length];
        int[] rightarray=new int[nums.length];
        int[] output= new int[nums.length];
        leftarray[0]=1;
        rightarray[nums.length-1]=1;
        for(int i=1;i<nums.length;i++)
        {
            leftproduct = leftproduct*nums[i-1];
            leftarray[i]=leftproduct;
        }
        for(int i=(nums.length)-2;i>=0;i--)
        {
            rightproduct=rightproduct*nums[i+1];
            rightarray[i]=rightproduct;
        }
        
        for(int i=0;i<nums.length;i++)
        {
            output[i]= leftarray[i]*rightarray[i];
        }
        return output;
            
        
    }
}