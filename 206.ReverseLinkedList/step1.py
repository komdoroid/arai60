class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = deque()
        dummy = ListNode(0)
        node = dummy

        while head:
            stack.append(head)
            head = head.next
        
        while stack:
            node.next = stack.pop()
            node = node.next
        node.next = None
        
        return dummy.next
