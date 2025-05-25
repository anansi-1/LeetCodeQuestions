class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans = []
        def dfs(s):
            if len(s) == n:
                ans.append(s)
                return
            dfs(s + '1')
            if not s or s[-1] != '0':
                dfs(s + '0')
        dfs("")
        return ans
