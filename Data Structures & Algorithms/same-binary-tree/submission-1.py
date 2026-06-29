# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        p = deque([p])
        q = deque([q])
        
        while p and q:
            node_p = p.popleft()
            node_q = q.popleft()

            # Both None → same, skip
            if not node_p and not node_q:
                continue
            # One None → different
            if not node_p or not node_q:
                return False
            # Values differ → different
            if node_p.val != node_q.val:
                return False
            p.append(node_p.left)
            p.append(node_p.right)
            q.append(node_q.left)
            q.append(node_q.right)

        return True


        
