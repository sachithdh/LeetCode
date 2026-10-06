class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        c = 0
        for i in s:
            if i == '(':
                stack.append(i)
            elif i == ")":
                if stack:
                    if stack[-1] == "(":
                        stack.pop()
                    else:
                        stack.pop()
                        c += 1
                else:
                    c+= 1

        return c + len(stack)