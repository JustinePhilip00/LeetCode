class Solution:
    def mySqrt(self, x: int) -> int:
        # diff_so_far = float("inf");
        # num = float("inf")
        # for i in range(0, x+1):
        #     if i*i <= x:
        #         num = i;
        #     else:
        #         break;
        # return num
        if x<2:
            return x;
        left = 0;
        right = x//2;
        while left<=right:
            mid = (left+right)//2;
            if mid*mid == x:
                return mid;
            elif mid*mid < x:
                left = mid +1;
            else:
                right = mid -1;
        return right;





