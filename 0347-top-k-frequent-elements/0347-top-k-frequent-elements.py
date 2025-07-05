class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count={};
        # freq = [[] for i in range(len(nums)+1)];
        
        # for num in nums:
        #     count[num] = 1+count.get(num,0);
        # print(count)
        # for num,c in count.items():
        #     freq[c].append(num);
        # print(freq);
        # res=[];
        # for i in range(len(freq)-1,0,-1):
        #     for num in freq[i]:
        #         res.append(num);
        #         if len(res) == k:
        #             print(res);
        #             return res;
        count ={};
        freq = [[] for i in range(len(nums)+1)];
        for num in nums:
            count[num] = 1+count.get(num,0);
        for num,c in count.items():
            freq[c].append(num);
        res =[];
        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                res.append(num);
                if len(res) == k:
                    return res;
        # count = {};
        # for num in nums:
        #     count[num] = 1+count.get(num, 0);
        # heap = [];
        # for num, freq in count.items():
        #     heapq.heappush(heap, (freq,num));
        # res =[];
        # while len(heap) > k:
        #     heapq.heappop(heap);
        # res= [];
        # print(heap);
        # for i in range(k):
        #     res.append(heapq.heappop(heap)[1])
        # return res;
        # mymap ={};
        # res =[];
        # for num in nums:
        #     mymap[num] = 1+mymap.get(num, 0);
        # while len(res) < k:
        #     top = max(mymap, key = mymap.get);
        #     # print(top)
        #     res.append(top);
        #     mymap.pop(top);
        # return res;


            
            
        