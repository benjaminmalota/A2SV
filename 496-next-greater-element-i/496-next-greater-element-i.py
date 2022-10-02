class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        ans= [-1] * len(nums1)
        for i in range(len(nums2)):
            x = nums2[i]
            while stack and stack[-1] < x:
                popped = stack.pop()
                index = nums1.index(popped)
                ans[index] = x
                
            if x in nums1:
                stack.append(x)
            else:
                continue 
      
        return ans