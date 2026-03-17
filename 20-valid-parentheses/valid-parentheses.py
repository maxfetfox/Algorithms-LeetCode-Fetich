class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = []
        for i in range(len(s)):
            if s[i] in '({[':
                stack.append(s[i])
            elif len(stack) > 0:
                if stack[-1] == '(' and s[i] == ')' or stack[-1] == '[' and s[i] == ']' or stack[-1] == '{' and s[
                    i] == '}':
                    stack.pop()
                else:
                    return False
            else:
                return False
        if len(stack) > 0:
            return False
        return True