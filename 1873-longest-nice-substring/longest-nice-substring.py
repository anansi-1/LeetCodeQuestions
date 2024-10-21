class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        n = len(s)
        length = 0
        start = -1
        unique_range = len(set(s))
        
        for unique in range(1, unique_range + 1):
            total = [0] * 26
            upper = [0] * 26
            lower = [0] * 26
            count_lower = 0
            count_upper = 0
            unique_count = 0
            left = 0
            
            for right in range(n):
                if s[right].isupper():
                    unique_count += total[ord(s[right]) - ord('A')] == 0
                    count_upper += upper[ord(s[right]) - ord('A')] == 0
                    total[ord(s[right]) - ord('A')] += 1
                    upper[ord(s[right]) - ord('A')] += 1
                else:
                    unique_count += total[ord(s[right]) - ord('a')] == 0
                    count_lower += lower[ord(s[right]) - ord('a')] == 0
                    total[ord(s[right]) - ord('a')] += 1
                    lower[ord(s[right]) - ord('a')] += 1
                
                while unique_count > unique:
                    if s[left].isupper():
                        unique_count -= total[ord(s[left]) - ord('A')] == 1
                        count_upper -= upper[ord(s[left]) - ord('A')] == 1
                        total[ord(s[left]) - ord('A')] -= 1
                        upper[ord(s[left]) - ord('A')] -= 1
                    else:
                        unique_count -= total[ord(s[left]) - ord('a')] == 1
                        count_lower -= lower[ord(s[left]) - ord('a')] == 1
                        total[ord(s[left]) - ord('a')] -= 1
                        lower[ord(s[left]) - ord('a')] -= 1
                    
                    left += 1
                
                if unique_count == count_lower == count_upper and (right - left + 1) > length:
                    length = right - left + 1
                    start = left
        
        return "" if start == -1 else s[start:start + length]
