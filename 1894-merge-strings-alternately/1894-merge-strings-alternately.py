class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output="";
        itr = 0;
        for i in range(min(len(word1),len(word2))):
            output = output+word1[i]+word2[i];
            itr =itr+1;
        # print(output)

        if itr < len(word1):
            output = output+ word1[itr:];
        elif itr < len(word2):
            output = output + word2[itr:]
        
        return output