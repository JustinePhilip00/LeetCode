class Solution:
    def reverse(self, x: int) -> int:
        if x<0:
            sign = -1;
        else:
            sign = 1;
        
        x= abs(x);
        reversed_int = int(str(x)[::-1]);
        reversed_int = sign*reversed_int;

        if reversed_int>2**31 or reversed_int < (-2**31):
            return 0;
        return reversed_int;