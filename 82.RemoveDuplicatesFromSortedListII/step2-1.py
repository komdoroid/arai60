class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 先頭の要素が重複している場合、重複しない要素まで移動する
        while head and head.next and head.val == head.next.val:
            duplicate_val = head.val
            while head and head.val == duplicate_val:
                head = head.next
            
        if not head:
            return None

        unique = head
        node = head.next

        while node:
            if node.next and node.val == node.next.val:
                duplicate_val = node.val
                while node and node.val == duplicate_val:
                    node = node.next
                unique.next = node
            
            else:
                unique = node
                node = node.next
        return head
