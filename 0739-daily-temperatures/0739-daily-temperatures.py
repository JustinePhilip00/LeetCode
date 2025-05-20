class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # O(n^2) way
        # output= [];
        # for i in range(len(temperatures)):
        #     for j in range(i+1,len(temperatures)):
        #         if temperatures[j] > temperatures[i]:
        #             output.append(j-i);
        #             break;
        #     else:
        #         output.append(0)
        # return output;
        output = [0]*len(temperatures); 
        stack = [];
        for i, t in enumerate(temperatures):
            while stack and t>stack[-1][0]:
                stackT, stackInd = stack.pop();
                output[stackInd] = (i-stackInd);
            stack.append([t,i]);
        return output;