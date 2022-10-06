class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ["a","e", "i", "o", "u"]
        res = 0
        r = k-1
        for i in range(k):
            if s[i] in vowels:
                res+=1
        l = 0
        v = res
        print(v)
        while r < len(s)-1:
            if s[l] in vowels:
                res-=1
            l+=1
            r+=1
            if s[r] in vowels:
                res += 1
            print(v)
            v = max(v, res)
        return v
        
                
                
                
            
            
            
            
                
                
                