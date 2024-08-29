class Solution:
    def romanToInt(self, s: str) -> int:
        romanNumerals = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        numeralValue = 0
        for index,value in enumerate(s):
            if index < len(s) - 1 and romanNumerals.get(value) < romanNumerals.get(s[index+1]):
                numeralValue -= int(romanNumerals.get(value))
            else:
                numeralValue += int(romanNumerals.get(value))
        return numeralValue
    
