class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        presum = [0]
        total = sum(nums)
    
        for i in range(len(nums)):
            presum.append(nums[i]+presum[i])
            if presum[i]==(total-nums[i]-presum[i]):
                return i
            
        return -1
            