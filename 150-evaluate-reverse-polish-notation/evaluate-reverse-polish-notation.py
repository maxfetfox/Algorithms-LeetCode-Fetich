class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        
        for item in tokens:
            if item == '+':
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num1 + num2)

            elif item == '*':
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num1 * num2)

            elif item == '-':
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2 - num1)

            elif item == '/':
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(int(num2 / num1)) # только такая реализация, потому что целочисленное деление работает как floor

            else:
                stack.append(int(item))
        return stack[0]