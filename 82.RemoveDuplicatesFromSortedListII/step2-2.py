class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        if head.next and head.val == head.next.val:
            duplicate_val = head.val
            while head and head.val == duplicate_val:
                head = head.next
            return self.deleteDuplicates(head)
        
        head.next = self.deleteDuplicates(head.next)
        return head
