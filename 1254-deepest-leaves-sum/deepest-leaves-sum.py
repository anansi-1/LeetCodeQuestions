# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque()
        q.append(root)
        while q:
            temp = 0
            for i in range(len(q)):
                cur = q.popleft() 
                if cur.left:
                    q.append(cur.left) 
                if cur.right:
                    q.append(cur.right)
                temp += cur.val
        return temp