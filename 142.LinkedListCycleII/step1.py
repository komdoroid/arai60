class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node_to_index = {}
        tail = head
        index = 0

        while tail:
            if tail in node_to_index:
                return tail
            node_to_index[tail] = index
            tail = tail.next
            index += 1
        
        return None
 