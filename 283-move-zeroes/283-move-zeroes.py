class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p1 = 0
        p2 = len(nums)
        
        while p1 < p2:
            if nums[p1] == 0:
                nums.append(nums.pop(p1))
                p2 -= 1
            else:
                p1 += 1
        