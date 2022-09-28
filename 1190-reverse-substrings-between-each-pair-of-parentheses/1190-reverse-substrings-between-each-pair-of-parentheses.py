class Solution:
     def reverseParentheses(self, s: str) -> str:
            
        stack =[]
        for i in s:
            if i == '(' or i.isalpha():
                stack.append(i)
            else:
                string = ""
                while len(stack)>0:
                    popped = stack.pop()
                    if popped == ")" or popped == "(":
                        break
                    string = popped + string
                string = string[::-1]
                
                for i in string:
                    stack.append(i)
        string = ""
        for i in stack:
            string = string + i
        
        return string
            
                