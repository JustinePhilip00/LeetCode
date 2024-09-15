class Solution {
    public boolean canJump(int[] nums) {
        int curPos = nums.length-1;
        for(int i=nums.length-2;i>=0;i--){
            if(i+nums[i]>=curPos)
                {
                    curPos=i;
                }
        }
        if(curPos==0){
            return true;
        }
        return false;
    }
}