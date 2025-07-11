def removeStars(self, s):
    """
    :type s: str
    :rtype: str
    """
    stack = []

    for char in s:
        if char == '*':
            stack.pop()
        else:
            stack.append(char)

    return ''.join(stack)
