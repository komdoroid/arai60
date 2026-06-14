class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        node_and_depth = [(root, 1)]
        max_depth = 0

        while node_and_depth:
            node, current_depth = node_and_depth.pop()
            if node:
                max_depth = max(current_depth, max_depth)
                if node.left:
                    node_and_depth.append((node.left, current_depth + 1))
                if node.right:
                    node_and_depth.append((node.right, current_depth + 1))

        return max_depth
