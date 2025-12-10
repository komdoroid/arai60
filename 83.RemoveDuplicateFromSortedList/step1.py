class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        unique_nodes = ListNode(0)
        current_node = unique_nodes
        node = head
        next_node = head.next

        while node:
            if not next_node:
                current_node.next = node
                break
            elif node.val != next_node.val:
                current_node.next = node
                current_node = current_node.next
            node = node.next
            next_node = next_node.next
        
        return unique_nodes.next
