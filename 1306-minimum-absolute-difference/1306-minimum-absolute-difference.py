class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort();
        # print(arr)
        output = [];
        maxMin = float('inf');
        for i in range(1, len(arr)):
            curMin = arr[i]-arr[i-1];
            if curMin < maxMin:
                maxMin = curMin;
                output = [[arr[i-1], arr[i]]];
            elif curMin == maxMin:
                output.append([arr[i-1], arr[i]]);
        return output;

        # arr.sort();
        # mydict = defaultdict(list);
        # for i in range(1, len(arr)):
        #     diff = arr[i]-arr[i-1];
        #     mydict[diff].append([arr[i-1],arr[i]]);
        # minkey = min(mydict)
        # return mydict[minkey]

        

        