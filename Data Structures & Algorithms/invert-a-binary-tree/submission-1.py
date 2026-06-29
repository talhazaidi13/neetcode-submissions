# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ### Depth firt search
        # if not root:
        #     return None
        # tmp = root.left
        # root.left = root.right
        # root.right = tmp
        # self.invertTree (root.left)
        # self.invertTree (root.right)
        # return root 

        ### Breadth first search
        if not root:
            return None
        quee = deque([root])
        while quee:
            node = quee.popleft()
            node.left, node.right = node.right , node.left
            if node.left:
                quee.append(node.left)
            if node.right:
                quee.append(node.right)
        return root
