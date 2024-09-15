class Solution {
    public int uniquePaths(int m, int n) {
        // if(m==0 || n==0){
        //     return 0;
        // }
        // if(m==1 && n==1){
        //     return 1;
        // }
        // return uniquePaths(m,n-1)+uniquePaths(m-1,n);
        
        int[][] dp = new int[m][n];
        for(int i=0;i<n;i++)
        {
            dp[m-1][i]=1;
        }
        for(int j=0;j<m;j++){
            dp[j][n-1]=1;
        }
        for(int i=m-2;i>=0;i--){
            for(int j=n-2;j>=0;j--){
                dp[i][j]=dp[i][j+1]+dp[i+1][j];
            }
        }
        return dp[0][0];
        
    }
}