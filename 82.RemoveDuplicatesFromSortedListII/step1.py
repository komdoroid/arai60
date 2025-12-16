class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        last_fixed_node = dummy

        while head:
            if head.next and head.val == head.next.val:
                duplicate_val = head.val
                while head and head.val == duplicate_val:
                    head = head.next
                last_fixed_node.next = head
            else:
                head = head.next
                last_fixed_node = last_fixed_node.next
            
        return dummy.next
