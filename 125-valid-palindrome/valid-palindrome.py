class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans = ""
        for i in s:
            if i.isalnum():
                ans += i.lower()
        i = 0
        j = len(ans) - 1

        while i < j:
            if ans[i] ==  ans[j]:
                i += 1
                j -= 1
            else:
                return False
        return True