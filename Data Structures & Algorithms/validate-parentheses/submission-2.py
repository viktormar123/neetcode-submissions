class Solution:
    def isValid(self, s: str) -> bool:
        open_char = ['(', '{', '[']
        closed_char = [')', '}', ']']
        stack = []

        for char in s:
            if char in open_char:
                stack.append(char)
            if char in closed_char:
                if stack:
                    if stack[-1] == open_char[closed_char.index(char)]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        if stack:
            return False
        else:
            return True
        
