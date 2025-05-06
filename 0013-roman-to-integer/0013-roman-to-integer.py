class Solution:
    def romanToInt(self, s: str) -> int:
        mymap = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
        }

        total =0;
        prevVal =0;
        for char in reversed(s):
            currVal = mymap[char];
            if currVal < prevVal:
                total = total - currVal;
            else:
                total = total + currVal;
            prevVal = currVal;
        return total; 