class Solution {
    public int maxArea(int[] height) {
       
        int h1= 0;
        int h2= height.length-1;
        int size = height.length;
        int maxarea=0;
        
        while(h1<h2)
        {
            int area = Math.min(height[h1],height[h2]) * (h2-h1);  
            maxarea = Math.max(maxarea,area);
            
        if(height[h1]<height[h2])
        {
            h1++;
        }
        else
        {
            h2--;
        }
        
    }
        return maxarea;
    }
}
        
        
        
        
       