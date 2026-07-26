# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        root = TreeNode()
        stack = [(0, len(nums) - 1, root)]

        while stack:
            left, right, node = stack.pop()
            mid = (left + right) // 2
            node.val = nums[mid]
            if left < mid:
                node.left = TreeNode()
                stack.append((left, mid - 1, node.left))
            if right < mid:
                node.right = TreeNode()
                stack.append((mid + 1, right, node.right))

        return root
