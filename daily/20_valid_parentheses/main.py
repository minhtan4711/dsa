class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if (c == "(" or c == "[" or c == "{"):
                stack.append(c)
            else:
                if stack:
                    testStr = stack[-1] + c
                    if testStr == "()" or testStr == "[]" or testStr == "{}":
                        stack.pop()
                    else:
                        return False
                else:
                    stack.append(c)
        if stack:
            return False
        return True
