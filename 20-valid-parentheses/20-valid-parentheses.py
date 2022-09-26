class Solution(object):
    def isValid(self, s):
        dic = {
            ")":"(",
            "}":"{",
            "]":"["
        }
        stack = []
        for i in s:
            if i in dic.values():
                stack.append(i)
            elif stack and dic[i] == stack[-1]:
                stack.pop()
            else:
                return False
        return stack == []