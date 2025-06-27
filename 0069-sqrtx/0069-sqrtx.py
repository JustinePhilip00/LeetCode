class Solution:
    def mySqrt(self, x: int) -> int:
        # diff_so_far = float("inf");
        num = float("inf")
        for i in range(0, x+1):
            if i*i <= x:
                num = i;
            else:
                break;
        return num




