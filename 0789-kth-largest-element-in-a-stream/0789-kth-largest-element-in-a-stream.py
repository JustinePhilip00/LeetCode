# better
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k;
        self.nums = nums;
        heapq.heapify(self.nums);
        while len(self.nums) > k:
            heapq.heappop(self.nums);
 
    def add(self, val: int) -> int:
        heapq.heappush(self.nums,val);
        if len(self.nums) > self.k:
            heapq.heappop(self.nums);
        return self.nums[0];
    

#     Slower 
# class KthLargest:

#     def __init__(self, k: int, nums: List[int]):
#         self.k = k;
#         self.nums = nums;
        

#     def add(self, val: int) -> int:
#         self.nums.append(val);
#         self.nums.sort();
#         return self.nums[len(self.nums)-self.k];

        

        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)