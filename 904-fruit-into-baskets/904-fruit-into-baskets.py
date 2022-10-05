class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        start = 0
        result = 0
        d = {}
        
        for r in range(len(fruits)):
            curr = fruits[r]
            if curr not in d:
                d[fruits[r]] = 0
            d[curr] += 1
            
            while len(d) > 2:
                if fruits[start] in d:
                    d[fruits[start]] -= 1
                    if d[fruits[start]] == 0:
                        del d[fruits[start]]
                start += 1
            result = max(result, r-start+1)
        
        return result