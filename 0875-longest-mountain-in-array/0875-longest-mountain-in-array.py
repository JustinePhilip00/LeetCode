class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        if len(arr)<3:
            return 0;
        maxlength =0;
        i=1;
        while i<len(arr)-1:
            if arr[i-1]<arr[i]>arr[i+1]:
                l=i-1;
                r=i+1;

                while l>0 and arr[l]>arr[l-1]:
                    l=l-1;
                while r<len(arr)-1 and arr[r]>arr[r+1]:
                    r=r+1;
                
                length = r-l+1;
                maxlength = max(maxlength, length);

                i=r;

            else:
                i=i+1;   
        return maxlength;
            



