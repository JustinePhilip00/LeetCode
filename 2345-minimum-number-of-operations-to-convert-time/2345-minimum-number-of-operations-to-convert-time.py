class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        # tomin = 
        totalcurrent = int(current[0:2])*60 + int(current[3:len(current)]);
        totalcorrect = int(correct[0:2])*60 + int(correct[3:len(correct)]);
        totaldiff = totalcorrect - totalcurrent;
        count = 0;
        for step in [60,15,5,1]:
            count = count + totaldiff//step;
            totaldiff = totaldiff%step;
        return count;

