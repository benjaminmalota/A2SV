class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        for items in range(1,n+1):
            if items% 3== 0 and items%5==0:
                result.append("FizzBuzz")
            elif items % 5 == 0:
                result.append("Buzz")
            elif items % 3 == 0:
                result.append("Fizz")
            else:
                result.append(str(items))
        return result
                
lo = Solution()
print(lo.fizzBuzz(15))