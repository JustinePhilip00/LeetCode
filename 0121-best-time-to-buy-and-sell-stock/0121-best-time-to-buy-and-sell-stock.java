class Solution {
    public int maxProfit(int[] prices) {
//         int lowestprice=prices[0];
//         int highestprice=0;
//         int profit=0;
//         boolean buy=false;
//         boolean sell=false;
//         int lowstoreindex=0;
//         int hightstoreindex=0;
//         for(int i=0;i<prices.length;i++)
//         {
//             if(prices[i]<=lowestprice)
//             {
//                 lowestprice=prices[i];
//                 lowstoreindex=i;
//                 buy=true;
//             }
//         }
//         if(buy==true)
//         {
//             for(int j=lowstoreindex;j<prices.length;j++)
//             {
//                 if(prices[j]>highestprice)
//                 {
//                     highestprice=prices[j];
//                     hightstoreindex=j;
//                     sell=true;
//                 }
//             }
//         }
//         if(sell==true)
//         {
//             profit=prices[hightstoreindex]-prices[lowstoreindex];
            
//         }
//         return profit;
//     }
        
        int profit=0;
        int calcprofit=0;
        int min=Integer.MAX_VALUE;
        for(int i=0;i<prices.length;i++)
        {
            if(prices[i]<min)
            {
                min=prices[i];
            }
            else if((prices[i]-min)>profit)
            {
                profit = prices[i]-min;
            }
        }
        return profit;
}
}