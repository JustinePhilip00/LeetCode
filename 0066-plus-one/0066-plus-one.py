class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = int(''.join(map(str, digits)))
        result = result+1;
        outputlist = [int(x) for x in str(result)];
        return outputlist;
        