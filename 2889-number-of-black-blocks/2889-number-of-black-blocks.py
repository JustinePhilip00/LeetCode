class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        blockCount = defaultdict(int);

        for x,y in coordinates:
            if x<m-1 and y<n-1:
                blockCount[(x,y)]= blockCount[(x,y)]+1;
            if x<m-1 and y>0:
                blockCount[(x,y-1)] = blockCount[(x,y-1)]+1;
            if x>0 and y<n-1:
                blockCount[(x-1,y)] =blockCount[(x-1,y)]+1;
            
            if x>0 and y>0:
                blockCount[(x-1, y-1)] = blockCount[(x-1, y-1)]+ 1;
        
        res = [0]*5;
        for count in blockCount.values():
            res[count] =  res[count]+1;
        
        totalBlocks = (m-1)*(n-1)
        res[0] = totalBlocks - sum(res[1:])
        
        return res


        