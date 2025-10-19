class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        ranges.sort();
        output= [];
        startpt = ranges[0][0];
        endpt=ranges[0][1];
        count = 0;
        if len(ranges)==1:
            return 2;
        for i in range(1,len(ranges)):
            start = ranges[i][0];
            if start<=endpt:
                endpt=max(endpt,ranges[i][1]);
            else:
                # output.append([startpt,endpt]);
                count= count+1;
                startpt = ranges[i][0];
                endpt=ranges[i][1];
            # output.append([startpt,endpt]);
        count=count+1
        return pow(2,count,10**9 + 7);



            


