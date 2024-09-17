class Solution {
//     public int lengthOfLIS(int[] nums) {
//         int [] dp = new int[nums.length+1];
//         // dp[nums.length-1] = 1;
//          int maximumSoFar = 1;
//         Arrays.fill(dp,1);
//         for(int i=nums.length-1;i>=0;i--){
//             for(int j=i+1;j<nums.length;j++)
//             {
//                 if(nums[i]<nums[j]){
//                     dp[i]=Math.max(dp[i],1+dp[j]);
//                     System.out.println("i value"+ i);
//                     System.out.println("j value"+j);
//                     System.out.println(dp[i]);
//                 }
                
//             }
//             maximumSoFar = Math.max(maximumSoFar, dp[i]);
            
//         }
//         return maximumSoFar;
//     }
     public int lengthOfLIS(int[] nums) {
        List<Integer> lis = new ArrayList<>(nums.length);

        for (int n : nums) {
            int i = Collections.binarySearch(lis, n);
            if (i < 0) i = -i - 1;

            if (i == lis.size())
                lis.add(n);
            else
                lis.set(i, n);
        }
        return lis.size();
    }
}
