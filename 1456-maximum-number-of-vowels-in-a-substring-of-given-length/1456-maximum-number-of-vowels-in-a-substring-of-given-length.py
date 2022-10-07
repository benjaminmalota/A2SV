class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        ans = 0
        curr = 0
        vowels = "aeiou"
        
        for r in range(len(s)):
            if r >= k:
                if s[r-k] in vowels:
                    curr -= 1
            if s[r] in vowels:
                curr += 1
            
            ans = max(ans, curr)
        return ans