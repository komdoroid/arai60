## step1
### 問題の理解
- LinkedListが与えられる
- 循環していた場合は循環の開始地点のListNodeを返す、循環していない場合はnullを返す

### 考えたこと
- "141. Linked List Cycle II"と似た問題。
- 前回はset()を使って解いたが、ListNodeはkeyとして使えるので辞書を用いる
- 辞書の必要が全くないので、やっぱりset()を使う。

### 計算量
ListNodeを終わりまでループして、辞書keyにすでに含まれる要素が出てくる or 最後まで重複しなければ終わり
- 時間計算量：O(n)
- 空間計算量：O(n)

### 辞書の場合(不要)
```python
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node_to_index = {}
        tail = head
        index = 0

        while tail:
            if tail in node_to_index:
                return tail
            node_to_index[tail] = index
            tail = tail.next
            index += 1
        
        return None
```

### setの場合
```python
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen = set()
        tail = head

        while tail:
            if tail in seen:
                return tail
            seen.add(tail)
            tail = tail.next
        
        return None
```

## step2
https://discord.com/channels/1084280443945353267/1246383603122966570/1252209488815984710
- フロイドの循環検出でも解けることを知った。
https://leetcode.com/problems/linked-list-cycle-ii/solutions/3274329/clean-codes-full-explanation-floyd-s-cycle-finding-algorithm-c-java-python3/
- slowとfastが衝突したとき、"出発地点から衝突地点 = 衝突地点から循環をして再度衝突地点"となる(fastは2倍の速さで進んでいるため)
- 循環の合流地点から衝突地点までは共通の道のりなので、考慮から除外すると"出発地点から合流地点 = 衝突地点から循環して合流地点"
https://docs.google.com/document/d/11HV35ADPo9QxJOpJQ24FcZvtvioli770WWdZZDaLOfg/edit?tab=t.0#heading=h.9kpbwslvv3yv
- 他の参加者のPRにコードの整え方についての指摘が多いので考慮する
https://github.com/aki235/Arai60/pull/2#discussion_r2599451331
- この問題とは関係ないが、自分でもコメントできるように心がける

```python
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head

        # fastの次が存在しないなら循環無し
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        
        return None
```

### 関数を使って書いてみる
https://github.com/nanae772/leetcode-arai60/pull/3#discussion_r2317374235
```python
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def getConfluencePoint(node):
            slow = fast = node
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
                if slow == fast:
                    return slow
            return None
        
        confluence = getConfluencePoint(head)
        if not confluence:
            return None
        start = head
        while start != confluence:
            start = start.next
            confluence = confluence.next
        return start
```

## step3
フロイドの循環検出を用いた方法で3回書く
