class Solution {
    public int rob(int[] nums) {
        if(nums.length==0){
            return 0;
        }
        if(nums.length ==1){
            return nums[0];
        }
        return Math.max(houserobber1(nums,0,nums.length-2), houserobber1(nums,1,nums.length-1)); 
    }
    
    public int houserobber1(int[] nums, int start,int end )
        {
            int rob1=0;
            int rob2=0;
            for(int i=start;i<=end;i++)
                {
                    int temp = Math.max(nums[i]+rob1,rob2);
                    rob1=rob2;
                    rob2= temp;
                }
                return rob2;
        }
    }
