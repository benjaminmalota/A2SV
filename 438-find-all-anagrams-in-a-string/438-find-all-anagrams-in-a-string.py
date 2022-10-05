class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        p2 = {} 
        l = 0
        d = {}
        res = []
        
        for i in p:
            p2[i] = 1 + p2.get(i, 0)
            
        for r in range(len(s)):
            d[s[r]] = 1 + d.get(s[r], 0)
            if (r-l+1) == len(p):
                if d == p2:
                    res.append(l)
                d[s[l]] -= 1
                if d[s[l]] == 0:
                    del d[s[l]]
                l+=1
        return res
                
                
            
