class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        # O(m*n)
        # output= [];
        # for q in queries:
        #     start = q[0];
        #     end = q[1];
        #     count=0;
        #     for i in range(start,end+1):
        #         # print("start",words[i][0]);
        #         # print("end",words[i][-1])
        #         if words[i][0] in 'aeiou' and words[i][-1] in 'aeiou':
        #             count = count+1;
        #     output.append(count);
        # return output;
        # O(n)
        vowel_set = set('aeiou')
        pref_cnt = [0]*(len(words)+1)
        prev = 0;
        for i, w in enumerate(words):
            if w[0] in vowel_set and w[-1] in vowel_set:
                prev = prev+1;
            pref_cnt[i+1] =prev;
        
        res = [0]*len(queries);
        for i, q in enumerate(queries):
            l,r = q;
            res[i] = pref_cnt[r+1] - pref_cnt[l];
        return res;
