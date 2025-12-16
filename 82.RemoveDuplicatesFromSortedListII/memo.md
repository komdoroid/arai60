## step1
### 問題の理解
- Linked listが与えられるので、その中から重複している要素は全て削除する。

### 考えたこと
- 重複していないことを確認してからnodeをつなげる
- ひとつ前の数字を記録する、一つ進んだ後前の数字と比べて一致していないかつ、さらに一つ後ろと比べて一致していないならば要素を追加する
- 記録していた数字を更新する
- うまくheadを更新して結果を作ることができなかったので、新しいListNodeを作る

### step0（未完成）
```py
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous_value = -1
        node = ListNode(-1)
        if not head:
            return head
        while head and head.next:
            if head.val != previous_value and head.val != head.next.val:
                node.next = head
                node = node.next
            previous_value = head.val
            head = head.next
        
        return node.next
```

実装がまとまらなかったので他の参加者のコードを見る
- https://github.com/aki235/Arai60/pull/4
- https://github.com/Yuto729/LeetCode_arai60/pull/11
- これらの完成形を参考にしてみる。
- 重複する要素については全てスキップして、重複終了までのポインタを保持する。重複していない場合はポインタを進める。
- この方針を参考にする。
- last_fixed_nodeという名前も参考にする

- どのnodeをどのタイミングで更新していけばよいか頭がなかなか整理できない。
- 更新されている変数とそうでないもの、それぞれの役割について混乱してしまう

```py
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
```

### 計算量について
- 時間計算量：O(n)
- 空間計算量：O(n)?
この場合、空間計算量はlast_fixed_nodeが更新されることを考慮する？

## step2
### 改善するときに考えたこと
1. 番兵を使わずに書いてみる(https://github.com/yus-yus/leetcode/pull/4#discussion_r1939063888)
2. 再帰で書けるかやってみる
3. while文の中身の書き方を変えてみる

1. 番兵を使わずに書いてみる
```py
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
```
- 最初、`unique = node`がすぐに理解できなかった。番兵を使う場合と少し混同していて、結果のためにuniqueから先の要素を更新しないといけないのになぜuniqueを更新するんだろう、と考えていた。
- 最終的には`head`を返すので、重複がなく`head`と要素の順番が同じ場合は更新の必要がない
- 「参照を動かす操作」と「構造を変更する動作」を区別する


2. 再帰で書けるかやってみる
- 再帰を書くのも苦手、、、AIと相談しつつ書いてみる
```py
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
```

3. while文の中身の書き方を変えてみる
- https://github.com/Yuto729/LeetCode_arai60/pull/11/files#r2572730796
これを参考に書き換える
```py
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        last_fixed_node = dummy

        while head:
            if head.next is None or head.val != head.next.val:
                head = head.next
                last_fixed_node = last_fixed_node.next
                continue
            duplicate_val = head.val
            while head and head.val == duplicate_val:
                head = head.next
            last_fixed_node.next = head
        
        return dummy.next
```
- 書いてみて個人的に思ったのは、書くときはstep1のほうが思考にそって書きやすくて、読むときは今回の場合のほうがそれぞれの場合を分けて考えられるので読みやすくて理解しやすい

4. 
- 長いので`last_fixed_node` -> `node`
```py
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        node = dummy

        while head is not None:
            if head.next is None or head.val != head.next.val:
                head = head.next
                node = node.next
                continue
            duplicate_val = head.val
            while head and head.val == duplicate_val:
                head = head.next
            node.next = head
        
        return dummy.next
```

## step3
"3. while文の中身の書き方を変えてみる"の方法で3回間違えずに書いてみる。
