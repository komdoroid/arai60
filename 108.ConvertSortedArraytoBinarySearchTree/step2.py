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

        def build_tree(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None
            mid = (left + right) // 2
            node = TreeNode(nums[mid])

            node.left = build_tree(left, mid - 1)
            node.right = build_tree(mid + 1, right)

            return node

        return build_tree(0, len(nums) - 1)
