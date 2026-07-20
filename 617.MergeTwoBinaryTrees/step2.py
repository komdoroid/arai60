class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None:
            return root2
        if root2 is None:
            return root1

        merged_value = root1.val + root2.val

        left_node = self.mergeTrees(root1.left, root2.left)
        right_node = self.mergeTrees(root1.right, root2.right)

        return TreeNode(merged_value, left_node, right_node)
