# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        node_and_depth = deque([(root, 1)])
        
        while node_and_depth:
            node, current_depth = node_and_depth.popleft()

            if node.left is None and node.right is None:
                return (current_depth)
            if node.left is not None:
                node_and_depth.append((node.left, current_depth + 1))
            if node.right is not None:
                node_and_depth.append((node.right, current_depth + 1))
