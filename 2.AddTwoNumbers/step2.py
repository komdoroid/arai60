class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode], carry: int = 0) -> Optional[ListNode]:
        if l1 is None and l2 is None and carry == 0:
            return None
        
        if l1 is None:
            digit1 = 0
        else:
            digit1 = l1.val
        if l2 is None:
            digit2 = 0
        else:
            digit2 = l2.val
        
        total = digit1 + digit2 + carry
        digit = total % 10
        carryNext = total // 10

        node = ListNode(digit)

        if l1 is None:
            next1 = None
        else:
            next1 = l1.next
        if l2 is None:
            next2 = None
        else:
            next2 = l2.next
        
        node.next = self.addTwoNumbers(next1, next2, carryNext)

        return node
