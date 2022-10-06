class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        l = 0
        r = len(cardPoints) - k
        sums = sum(cardPoints[r:])
        total = sums
        while r < len(cardPoints):
            sums += (cardPoints[l]-cardPoints[r])
            total = max(total, sums)
            l+=1
            r+=1
            
        return total