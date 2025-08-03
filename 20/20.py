class Solution:
    def isValid(self, s: str) -> bool:
        match = {')': '(', '}': '{', ']': '['}
        stack = []
        for l in s:
            if l in match.values():
                stack.append(l)
            elif l in match:
                if not stack or stack[-1] != match[l]:
                    return False
                stack.pop()
            else:
                return False
        return not stack
    
    
Solutionclass = Solution()
print(Solutionclass.isValid("()"))

# ()
# (){}
# (){}[]
# ([])
# ([})

