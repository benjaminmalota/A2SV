class Solution(object):
    def sortColors(self, nums):
        for i in range(len(nums)-1):
            for j in range(i,-1,-1):
                if nums[j] > nums[j+1]:
                    nums[j],nums[j+1] = nums[j+1],nums[j]
        return nums
        
        