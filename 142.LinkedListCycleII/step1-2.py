class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen = set()
        tail = head

        while tail:
            if tail in seen:
                return tail
            seen.add(tail)
            tail = tail.next
        
        return None
