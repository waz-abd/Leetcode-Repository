class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        pairs = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for ch in s:
            if ch not in pairs:
                stack.append(ch)
            else:

                if not stack:
                    return False
