def decodeString(self, s):
    """
    :type s: str
    :rtype: str
    """
    stack = []

    for char in s:
        if char != "]":
            stack.append(char)
        else:
            subString = ""
            while stack[-1] != "[":
                subString = stack.pop() + subString
            stack.pop()

            k = ""
            while stack and stack[-1].isdigit():
                k = stack.pop() + k
            stack.append(int(k) * subString)
    return "".join(stack)
