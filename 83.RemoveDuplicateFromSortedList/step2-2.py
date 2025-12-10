class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        if head.val == head.next.val:
            head.next = head.next.next
            return self.deleteDuplicates(head)
        
        head.next = self.deleteDuplicates(head.next)
        return head
