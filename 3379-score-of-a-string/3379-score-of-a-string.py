class Solution:
    def scoreOfString(self, s: str) -> int:
        ascii = {"a": 97,
                "b": 98, 
                "c":99,
                "d":100,
                "e":101,
                "f":102,
                "g":103,
                "h":104,
                "i":105,
                "j":106,
                "k":107,
                "l":108,
                "m":109,
                "n":110,
                "o":111,
                "p":112,
                "q":113,
                "r":114,
                "s":115,
                "t":116,
                "u":117,
                "v":118,
                "w":119,
                "x":120,
                "y":121,
                "z":122,
                }
        # total = 0;
        currscore =0;
        for i in range(len(s)):
            if i+1 < len(s):
                currscore=currscore+abs(ascii[s[i]] - ascii[s[i+1]]);
                # total = total +currscore;
        # return total;
        return currscore;

        