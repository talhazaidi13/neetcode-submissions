class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_bracket_dict = {")":"(",
                              "]":"[",
                              "}":"{"}
        for c in s:
            if c in close_bracket_dict:
                if stack and stack[-1] == close_bracket_dict[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False