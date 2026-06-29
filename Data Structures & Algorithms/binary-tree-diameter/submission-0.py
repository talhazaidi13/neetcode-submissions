# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
           
        self.child_len = 0
         
        def dfs(root):
           # base case
           if not root:
               return 0
           # Recursive
           left = dfs(root.left)
           right = dfs(root.right)
           # Calculate childlength
           self.child_len = max( self.child_len , (left + right))
           return 1 + max(left, right)

        dfs(root)
        return self.child_len