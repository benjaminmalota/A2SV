class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
    
        for i in asteroids:
            while stack and stack[-1] > 0 and i < 0:
                add = i + stack[-1]
                if add < 0:
                    stack.pop()
                elif add > 0:
                    i = 0
                else:
                    i = 0
                    stack.pop()
            if i:
                stack.append(i)
                
        return stack  
                    
                    
            