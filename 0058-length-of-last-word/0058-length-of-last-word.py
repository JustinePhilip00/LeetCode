class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        newStr = s.split();
        return len(newStr[-1]);