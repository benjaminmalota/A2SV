class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums2 = nums[::-1]
        prefix = [1]
        prefix2 = [1]
        answer = []
        for i in range(len(nums)):
            prefix.append(nums[i]*prefix[i])
            prefix2.append(nums2[i]*prefix2[i])
            if len(prefix) == len(nums)+1:
                prefix.remove(prefix[0])
                prefix2.remove(prefix2[0])
                prefix2=prefix2[::-1]
        
        for i in range(1,len(nums)-1):
            answer.append(prefix[i-1]*prefix2[i+1])
                        
        answer.append(prefix[-2])
        answer.insert(0,prefix2[1])
        
        return answer