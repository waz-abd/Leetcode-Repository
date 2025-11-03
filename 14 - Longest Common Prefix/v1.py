class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        short_word = min(strs, key=len)

        prefix = ""

        for i in range(len(short_word)):

            character = short_word[i]

            for word in strs:

                if word[i] != character:
                    return prefix

            prefix = prefix + character

        return prefix
