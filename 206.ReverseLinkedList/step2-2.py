class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        reversed_head = self.reverseList(head.next)
        not_reversed_node = head.next
        not_reversed_node.next = head
        head.next = None

        return reversed_head
