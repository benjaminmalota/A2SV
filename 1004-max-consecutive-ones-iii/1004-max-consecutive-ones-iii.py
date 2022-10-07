class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        res = 0
        
        for r,i in enumerate(nums):
            k = k-(1-i)
            if k<0:
                k = k + (1-nums[l])
                l+=1
            res = max(res, r - l + 1)
        return res
    
            