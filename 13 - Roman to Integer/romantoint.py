class Solution:
    def romanToInt(self, s: str) -> int:
        
        symbol = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        total = 0
        
        for i in range(len(s)):
            
            num = symbol[s[i]]

            if (i + 1 < len(s)) and (num < symbol[s[i + 1]]):
                total = total - num
                
            else:
                total = num + total
        
        return total