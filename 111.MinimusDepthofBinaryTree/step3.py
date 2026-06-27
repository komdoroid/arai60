class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        node_and_depth = deque([(root, 1)])

        while node_and_depth:
            node, current_depth = node_and_depth.popleft()
            if node.left is None and node.right is None:
                return current_depth
            if node.left is not None:
                node_and_depth.append((node.left, current_depth + 1))
            if node.right is not None:
                node_and_depth.append((node.right, current_depth + 1))

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        left_depth = self.minDepth(root.left)
        right_depth = self.minDepth(root.right)
        if left_depth == 0:
            return right_depth + 1
        if right_depth == 0:
            return left_depth + 1
        return min(left_depth, right_depth) + 1
