## step1
### 何を考えて解いたか
- Linked listを末尾まで見て、順番にstackに格納
- 最後まで格納出来たら、取り出した順につなげ直すという方針で解く

```py
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
        
        return dummy.next 
```
- 上記のコードは間違い
<https://github.com/Yuto729/LeetCode_arai60/pull/13/files#diff-9f1b7f383ffeff5062b1d2301870d582d917501c1dfa9d7a5f7be5ec68711bd6R19:~:text=tail.next.next%20%3D%20None>
- 最後の要素から次の要素へのつながりを消さないといけないことに気づかなかった

```py
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
```

### 計算量について
- 時間計算量：O(n)
- 空間計算量：O(n)


## step2
- 他の人のコードやコメント集を確認して、コードを改善。別の解き方も調べる

### すべてのLinkedListの要素を反転させる
- (参考にしたコード)https://github.com/aki235/Arai60/pull/7/commits/b99a88644d27afde2d6d2504e072ed27f2dfe015
- この中でスタックを使わず連結をすべて付け替える方法でコードを書いていた
- (名前の付け方について)https://github.com/tarinaihitori/leetcode/pull/6#discussion_r1811921288
- 明確に反転済みと、まだ反転されていない部分がわかるように変数名を付ける

```py
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
```

### 再帰で書いてみる
- (参考にしたコード)https://github.com/tarinaihitori/leetcode/pull/6/commits/7ae6c941f485e4fd52fab64cf17584150ea87d03#:~:text=%60%60%60-,%E9%81%8E%E5%8E%BB,-%E3%83%AD%E3%82%B0%E3%82%84%E3%81%BB%E3%81%8B
- これを一目見て理解できない
- まずは末尾を探して、見つけたらリターンしながらリストのリンクを逆向きに付け替えていくというのを何とか理解
- 以前、再帰の行きがけ/帰りがけ、どちらで処理を行うかみたいな話を理解しきれていなかったが、これが帰りがけの処理？

```py
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        reversed_head = self.reverseList(head.next)
        not_reversed_node = head.next
        not_reversed_node.next = head
        head.next = None

        return reversed_head
```

## step3
step2-1の方法で3回書く