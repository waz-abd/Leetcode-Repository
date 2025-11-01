class Solution:
    def isPalindrome(self, x: int) -> bool:

        string_x = str(x)

        for i in range(len(string_x)):
            if string_x[i] != string_x[len(string_x) - 1 - i]:
                return False
        return True
