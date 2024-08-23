class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        count = 0
        num_str = str(num)
        n = len(num_str) - k + 1

        for i in range(n):
            substring = num_str[i:i + k]
            toint = int(substring)

            if toint != 0 and num % toint == 0:
                count += 1
                
        return count
