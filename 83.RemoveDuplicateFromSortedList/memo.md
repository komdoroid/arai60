## step1
### 問題の理解
- ソートされたLinkedListから重複を削除する
- 重複が消えてソートされた状態のLinkedListを返す

### 考えたこと
- 重複を削除することからsetを使うことを考えたが、順番を維持するのに手間がかかりそうなのでやめる
- node.valが前回から変化しているかを判断して、変化している場合のみnode.nextとする
- 番兵を置いた方がやりやすいか？
- whileの中のif-elifがもっときれいにならないか？

### 計算量
時間計算量：O(n)
空間計算量：O(1)

```python
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
```

## step2
### 他の人のコードを読んで考えたこと
- https://github.com/tNita/arai60/pull/4
- https://github.com/Yuto729/LeetCode_arai60/pull/10
1つずつ要素を進めて、前後を比べる。という方針で進んでいたので`node`と`next_node`を置いたが、
数字が変わったときだけ更新するようにすれば、`node`のみでよい。
新しいリストも作成する必要がない、`node`に`head`を入れているのでこれにつなげていく。
```python
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        while node and node.next:
            if node.val == node.next.val:
                node.next = node.next.next
            else:
                node = node.next
        return head
```

whileを再帰で書き換える
```python
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        if head.val == head.next.val:
            head.next = head.next.next
            return self.deleteDuplicates(head)
        
        head.next = self.deleteDuplicates(head.next)
        return head
```

## step3
step2のコードを間違えずに3回書く
