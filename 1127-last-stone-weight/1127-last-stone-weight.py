class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # stones = [-s for s in stones];
        # heapq.heapify(stones);
        # while len(stones)>1:
        #     first = heapq.heappop(stones);
        #     second = heapq.heappop(stones);
        #     if second>first:
        #         heapq.heappush(stones,first-second);
        # stones.append(0);
        # return abs(stones[0]);
        if len(stones)==1:
            return stones[0];
        if len(stones)==0:
            return 0;
        stones  = [-1 * stone for stone in stones ];
        # print(stones)
        heapq.heapify(stones);
        while len(stones)>1:
            stone1 = -1 * heapq.heappop(stones);
            stone2 = -1 * heapq.heappop(stones);
            if stone1 == stone2:
                continue;
            elif stone1<stone2:
                heapq.heappush(stones,-1*(stone1-stone2));
            elif stone2<stone1:
                heapq.heappush(stones,-1*(stone1-stone2));
        return -stones[0] if stones else 0;

