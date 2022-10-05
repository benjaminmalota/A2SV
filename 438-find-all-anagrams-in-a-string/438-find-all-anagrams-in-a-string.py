class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        target = {}
        for i in p:
            target[i] = 1 + target.get(i, 0)
        l = 0
        res = []
        string_counter = {}
        for r in range(len(s)):
            string_counter[s[r]] = 1 + string_counter.get(s[r], 0)
            if (r - l + 1) == len(p):
                if string_counter == target:
                    res.append(l)
                string_counter[s[l]] -= 1
                if string_counter[s[l]] < 1:
                    del string_counter[s[l]]
                l += 1
        return res