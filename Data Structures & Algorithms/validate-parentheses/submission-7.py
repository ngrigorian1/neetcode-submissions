class Solution:
    def isValid(self, s: str) -> bool:
        
        pairs = {"[":"]", "(":")", "{":"}"}
        stack = []

        if len(s) % 2 != 0:
            return False

        for c in s:
            if c in pairs:
                stack.append(c)
            else:
                if len(stack) == 0 or c != pairs[stack[-1]]:
                    return False
                stack.pop()
        
        if len(stack) != 0:
            return False
        return True