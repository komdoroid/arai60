class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def getConfluencePoint(node):
            slow = fast = node
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
                if slow == fast:
                    return slow
            return None
        
        confluence = getConfluencePoint(head)
        if not confluence:
            return None
        start = head
        while start != confluence:
            start = start.next
            confluence = confluence.next
        return start
