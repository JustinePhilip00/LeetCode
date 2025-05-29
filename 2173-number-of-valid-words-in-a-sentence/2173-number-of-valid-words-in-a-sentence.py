class Solution:
    def countValidWords(self, sentence: str) -> int:
        tokens = sentence.split();
        count = 0;
        for token in tokens:
            if any(char.isdigit() for char in token):
                continue
            elif "-" in token : 
                if token.count("-")>1:
                    continue;
                index = token.index("-");
                if index==0 or index==len(token)-1:
                    continue;
                if not (token[index - 1].islower() and token[index + 1].islower()):
                    continue 
            punctuations = "!.,";
            if sum(1 for ch in token if ch in punctuations)>1:
                continue;
            if any(ch in punctuations for ch in token[:-1]):
                continue;
            if not all(ch.islower() or ch in "-!,." for ch in token):
                continue;
            count =count+1;
        return count;
            


                
        
        
        
        
        return count;

            