class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # arr.sort();
        # print(arr)
        # output = [];
        # maxMin = arr[1]-arr[0];
        # l=0;
        # for r in range(1, len(arr)):
        #     curMin = arr[r]-arr[l];
        #     if curMin <= maxMin:
        #         maxMin = min(maxMin,curMin);
        #         output.append([arr[l],arr[r]]);
        #     l=l+1;
        # return output;
        arr.sort();
        mydict = defaultdict(list);
        for i in range(1, len(arr)):
            diff = arr[i]-arr[i-1];
            mydict[diff].append([arr[i-1],arr[i]]);
        minkey = min(mydict)
        return mydict[minkey]

        

        