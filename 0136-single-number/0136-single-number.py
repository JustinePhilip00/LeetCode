class Solution:
    def singleNumber(self, nums: List[int]) -> int:
#         using extra space
        seen =set();
        for num in nums:
            if num in seen:
                seen.remove(num);
            else:
                seen.add(num);
        return list(seen)[0];
    