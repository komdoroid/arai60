class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        not_reversed_head = head
        reversed_head = None

        while not_reversed_head:
            next_not_reversed = not_reversed_head.next
            not_reversed_head.next = reversed_head
            reversed_head = not_reversed_head
            not_reversed_head = next_not_reversed

        return reversed_head
