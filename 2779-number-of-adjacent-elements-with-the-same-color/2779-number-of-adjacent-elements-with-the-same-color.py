class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        arr = [0]*n;
        ans =[];
        sameColors =0
        for i,color in queries:
            if i+1<n:
                if arr[i+1]>0 and arr[i+1]==arr[i]:
                    sameColors = sameColors-1;
                if arr[i+1]==color:
                    sameColors= sameColors+1;
            if i>0:
                if arr[i-1]>0 and arr[i-1]==arr[i]:
                    sameColors = sameColors-1;
                if arr[i-1]==color:
                    sameColors = sameColors+1;
            arr[i] =color;
            ans.append(sameColors);
        return ans;


        

