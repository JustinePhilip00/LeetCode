class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort();
        output= [];
        start = intervals[0][0]
        end = intervals[0][1];
        if len(intervals) == 1:
            return intervals;
        for i in range(1, len(intervals)):
            pt = intervals[i][0];
            # if i==1 and pt>end:
            #     output.append(intervals[0])
            if pt<=end:
                end = max(end, intervals[i][1]);
                # output.append([start, end]);
            else:
                output.append([start, end]);
                start = intervals[i][0];
                end = intervals[i][1];
        output.append([start, end])
        return output;
