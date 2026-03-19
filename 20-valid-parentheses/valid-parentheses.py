class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0: # если количество скобок нечётно, у одной из скобок гарантированно нет пары
            return False

        stack = [] # сюда помещаются открывающие скобки

        for i in range(len(s)):
            if s[i] in '({[':
                stack.append(s[i])

            elif len(stack) > 0:
                if stack[-1] == '(' and s[i] == ')' or stack[-1] == '[' and s[i] == ']' or stack[-1] == '{' and s[
                    i] == '}':
                    stack.pop() # если закрывающая скобка совпадает с последней открывающей, то проверка переходит к следующей паре

                else:
                    return False # в случае несовпадения – False
            else:
                return False # если попалась сначала закрывающая скобка, затем открывающая, например: ')('
        if len(stack) > 0: # если стек не пуст, значит у части скобок не оказалось пары
            return False
        return True
