## step1
### 問題の理解
- Linked Listが与えられるので、それが循環しているかどうかを判定する
- True or Falseを返す
### 考えたこと
- 何をもってcycleを判定するのか？
- 次の要素の値がわかったとしても、それが循環している判定ができない
- 知識面で足りない部分がありそう
- わからないので調べる

--- 

- https://qiita.com/toshi_machine/items/3b2a5c04da949ac78298
上記の記事を参考
- PythonのListとLinked Listを似たようなものとして捉えていたため、set()で比較可能であるという発想にならなかった。
- hashで比較ができる
- ListNodeはオブジェクトなので比較はハッシュで行われる、という理解

```python
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        current = head

        while current:
            if current in seen:
                return True
            seen.add(current)
            current = current.next
        return False
```
### 計算量について
時間計算量：O(n)
空間計算量：O(n)

## step2
- 速度の違う２つのポインタを使うことで循環の確認が可能なので書いてみる
- ただし、有名なテクニックなので本質ではない
- https://discord.com/channels/1084280443945353267/1195700948786491403/1195944696665604156

```python
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False
```

- `fast = slow = head`はどうせ同じものを入れるならこの書き方のほうがわかりやすいと思った。

### step2-2
- step1はwhileを使っているので再帰に書き換えることもできる
```python
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()

        def dfs(node):
            if node is None:
                return False
            if node in seen:
                return True
            seen.add(node)
            return dfs(node.next)
        
        return dfs(head)
```

## step3
step1の方法で３回書く
