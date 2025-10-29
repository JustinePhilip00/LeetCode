class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        ROWS = len(box);
        COLS = len(box[0]);
        res= [["."]*ROWS for _ in range(COLS)];
        for r in range(ROWS):
            i = COLS -1;
            for c in reversed(range(COLS)):
                if box[r][c] == "#":
                    res[i][(ROWS-1)-r] = "#";
                    i=i-1;                
                elif box[r][c] =="*":
                    res[c][(ROWS-1)-r] = "*"
                    i=c-1;
        return res;
