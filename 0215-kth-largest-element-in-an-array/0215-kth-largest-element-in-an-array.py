class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nums= [-num for num in nums ];
        # heapq.heapify(nums);
        # cnt = 0;
        # if len(nums)==1:
        #     return abs(nums[0]);
        # while len(nums)>1:
        #     if cnt!=k-1:
        #         heapq.heappop(nums);
        #         cnt = cnt+1;
        #     if cnt == k-1:
        #         return abs(nums[0]);
        return heapq.nlargest(k, nums)[-1]

