class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        presum = [0]
        
        for i in range(len(nums)):
            presum.append(presum[i]+nums[i])
            if presum[i] == total-nums[i]-presum[i]:
                return i
        return -1
        