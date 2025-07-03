class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        countK = nums.count(k);
        res  = 0;
        for i in range(1,51):
            if i==k:
                continue;
            cnt = 0;
            for num in nums:
                if num == i:
                    cnt = cnt +1;
                if num ==k:
                    cnt = cnt-1;
                cnt = max(cnt,0);
                res = max(res, cnt+countK);
        return res;
            