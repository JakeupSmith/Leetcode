class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def func(s):
            stack = ''
            for i in s:
                if stack and i == '#':
                    stack = stack[:len(stack)-1]
                elif i != '#':
                    stack += i
            return stack
        return func(s) == func(t)
            