class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None:
            return root2
        elif root2 is None:
            return root1

        merged_tree = TreeNode(root1.val + root2.val)
        node1_node2_merged = deque([(root1, root2, merged_tree)])

        while node1_node2_merged:
            node1, node2, merged = node1_node2_merged.popleft()

            if node1 is None:
                node1 = TreeNode(0)

            if node2 is None:
                node2 = TreeNode(0)

            if node1.left is not None or node2.left is not None:
                val1 = node1.left.val if node1.left is not None else 0
                val2 = node2.left.val if node2.left is not None else 0
                new_left = TreeNode(val1 + val2)
                merged.left = new_left
                node1_node2_merged.append((node1.left, node2.left, new_left))

            if node1.right is not None or node2.right is not None:
                val1 = node1.right.val if node1.right is not None else 0
                val2 = node2.right.val if node2.right is not None else 0
                new_right = TreeNode(val1 + val2)
                merged.right = new_right
                node1_node2_merged.append((node1.right, node2.right, new_right))
        return merged_tree
