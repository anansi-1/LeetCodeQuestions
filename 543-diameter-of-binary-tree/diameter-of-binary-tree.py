# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        curr_max = 0

        def helper(node):
            nonlocal curr_max
            if node == None:
                return 0
            curr_left = helper(node.left)
            curr_right = helper(node.right) 
            curr_max = max(curr_max,curr_left+ curr_right)
            return 1 + max(curr_left,curr_right)
        helper(root)
        return curr_max