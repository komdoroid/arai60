class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()

        def dfs(node):
            if node is None:
                return False
            if node in seen:
                return True
            seen.add(node)
            return dfs(node.next)
        
        return dfs(head)
