# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    #      res = defaultdict(list)
    #      def dfs(node, depth):
    #         if not node:
    #             return None
    #         res[depth].append(node.val)
    #         dfs(node.left, depth+1)
    #         dfs(node.right, depth+1)

    #      dfs(root, 0)
    #      return  list(res.values())


    #### BFS
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        queue = deque([root])

        while queue:
            level = []
            for i in range(len(queue)):  # process exactly this level's nodes
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level)
        
        return res