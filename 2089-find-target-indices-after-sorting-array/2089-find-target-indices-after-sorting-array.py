class Solution(object):
    def targetIndices(self, nums, target):
        nums.sort()
        final = []
        for i in range(len(nums)):
            if nums[i] == target:
                final.append(i)
        return final
        