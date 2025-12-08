class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        current = head

        while current:
            if current in seen:
                return True
            seen.add(current)
            current = current.next
        return False
