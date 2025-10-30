class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)==1:
            return intervals;
        intervals.sort()
        output=[]
        start = intervals[0][0]
        end = intervals[0][1];
        for i in range(1, len(intervals)):
            startpt = intervals[i][0];
            if startpt<=end:
                end = max(end,intervals[i][1]);
            else:
                output.append([start, end]);
                start = intervals[i][0];
                end = intervals[i][1];
        output.append([start, end])
        return output;
        



            

