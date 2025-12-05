## step1
### 問題の理解
2つのLinked listが与えられる（空でない、負でない）、それらを足し合わせて答えをLinked listとして返す。
[Linked list](https://ja.wikipedia.org/wiki/%E9%80%A3%E7%B5%90%E3%83%AA%E3%82%B9%E3%83%88)
本問は自身の値と、次の要素へのリンクを持つ片方向リスト。

## 考えたこと
正直、Linked listの使い方があまりわからないので調べてみる。
Linked listを使用しない実装も考えてみる必要がある?

各要素を足し合わせて10を超えた場合は、次の要素に1を追加。現在の要素は10のあまりとすればできる？
具体的に実装できなかったので答えを調べる。
```python
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0)
        tail = dummyHead
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            digit1 = l1.val if l1 is not None else 0
            digit2 = l2.val if l2 is not None else 0

            sum = digit1 + digit2 + carry
            digit = sum % 10
            carry = sum // 10

            tail.next = ListNode(digit)
            tail = tail.next
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
        return dummyHead.next
```
結果を格納するListNodeを定義するのを思いつかなかった。
ListNodeを使ってtail.nextを定義するのは思いつかなかった。
また、returnがListNodeの先頭だけ返すのは納得感を持って理解しづらい。

## step2
### 改善するときに考えたこと
- whileを使わず書いてみたらどうか
- if-elseの書き方を変更する必要があるか
### 他の参加者のコードやコメントを見る
- https://github.com/Yuto729/LeetCode_arai60/pull/2/commits/26857b7af2a55de4795cf26ac5b313902226aca9#r2565050220
確かにその通りなので、`sum`は使わないように修正する

- https://docs.google.com/document/d/11HV35ADPo9QxJOpJQ24FcZvtvioli770WWdZZDaLOfg/edit?tab=t.0#heading=h.7zcdki273ah6
この書き方はたまに見かけるので、参考にしていたが正直わかりにくいと自分も思っていたので基本的には使わない書き方を選ぶことにする。

- https://discord.com/channels/1084280443945353267/1196472827457589338/1197166381146329208
> whileを使わずに書いてみたらどうか
再帰を使って書ける。さらに再帰はループに変換できる、そういう認識をもっていなかったのでどちらも実装してみる。
行きがけ、帰りがけの話が理解できない。
再帰処理が進むたびに、1桁数値が求められるのが行きがけ？とすれば帰りがけはどのような処理になるのか？
ループ中にstackに計算結果を積んで、最後に取り出しながら連結リストを作る？

- https://github.com/seal-azarashi/leetcode/pull/5#discussion_r1633585967
dammyを使わずに書く方法を考える。
まずコーディングにおける番兵という概念を初めて知った。
番兵は最初だけ特別な処理をするのを避けるために定義するものという理解。

- https://github.com/Yoshiki-Iwasa/Arai60/pull/4#discussion_r1644051434
この問題を3つ以上のLinkedListの足し算を行うように一般化したらどうなるか


### 再帰で解く場合
- carryも引数として渡せるようにする必要がある。
```python
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
        nextCarry = total // 10

        node = ListNode(digit)

        if l1 is None:
            next1 = None
        else:
            next1 = l1.next
        if l2 is None:
            next2 = None
        else:
            next2 = l2.next
        
        node.next = self.addTwoNumbers(next1, next2, nextCarry)

        return node
```

### dummyを使わない場合
- どちらにせよ始まりを保持する必要がある
```python
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        tail = None
        carry = 0
        while l1 is not None and l2 is not None and carry != 0:
            if l1 is None:
                digit1 = 0
            else:
                digit1 = l1.val
            if l2 if None:
                digit2 = 0
            else:
                digit2 = l2.val
            
            total = digit1 + digit2 + carry
            digit = total % 10
            carry = total // 10

            if l1 is None:
                l1 = None:
            else:
                l1 = l1.next
            if l2 is None:
                l2 = None
            else:
                l2 = l2.next
            
            node = ListNode(digit)
            if head is None:
                head = node
                tail = node
            else:
                tail.next = node
                tail = tail.next
        return head
```

## step3
再帰のパターンを間違えずに３回書く
