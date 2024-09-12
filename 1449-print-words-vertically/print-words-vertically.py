class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        max_length = max(len(word) for word in words)
        vertical_print = []
      
        for i in range(max_length):
            column_chars = [(word[i] if i < len(word) else ' ') for word in words]
            while column_chars and column_chars[-1] == ' ':
                column_chars.pop()
            vertical_print.append(''.join(column_chars))
      
        return vertical_print