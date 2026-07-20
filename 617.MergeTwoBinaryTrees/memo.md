# 617. Merge Two Binary Trees

## 何を考えて解いたか
２つのtreeをrootから順番に見て、要素の値を合計する。
そのためにどうするか？
tree1, tree2のnodeをそれぞれまとめた(node1, node2)のようなtupleを使って深さ優先探索をする。
どちらかが'None'でないなら、次を探索し続ける。両方'None'ならそこで終わり。
ここまで考えたけど、これだと最終的な出力のtreeのどの位置に値を入れたらいいかがわからない。
tupleに新しいtreeも含める。

## step1
いったんここまでの方針で書いてみる
```python
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None:
            return root2
        elif root2 is None:
            return root1

        merged_tree = TreeNode(root1.val + root2.val)
        node1_node2_merged = deque([(root1, root2, merged_tree)])

        while node1_node2_merged:
            node1, node2, merged = node1_node2_merged.popleft()
            if node1 is None:
                node1 = TreeNode(0)
            if node2 is None:
                node2 = TreeNode(0)
            if node1.left is not None or node2.left is not None:
                val1 = node1.left.val if node1.left is not None else 0
                val2 = node2.left.val if node2.left is not None else 0
                new_left = TreeNode(val1 + val2)
                merged.left = new_left
                node1_node2_merged.append((node1.left, node2.left, new_left))
            if node1.right is not None or node2.right is not None:
                val1 = node1.right.val if node1.right is not None else 0
                val2 = node2.right.val if node2.right is not None else 0
                new_right = TreeNode(val1 + val2)
                merged.right = new_right
                node1_node2_merged.append((node1.right, node2.right, new_right))
        return merged_tree
```

## step2
- https://github.com/goto-untrapped/Arai60/pull/47/changes/8757cd56cd9b23fcd4e33d9b5abfb38b26dfad39
現状のコードだと中途半端に破壊的？`return root2`, `return root1`としているところがあるので入力元のメモリが書き換わると出力した結果も変わる。

完全に非破壊でやるなら入力のtreeをcloneして返す。

破壊的にやればメモリが節約されるが、参照している値が書き換わると意図しない箇所まで影響する可能性がある。非破壊的にやればメモリが多く消費されるが、安全。

再帰で書くとかなりシンプルになるようなので再帰で書いてみる。

```python
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None:
            return root2
        if root2 is None:
            return root1

        merged_value = root1.val + root2.val

        left_node = self.mergeTrees(root1.left, root2.left)
        right_node = self.mergeTrees(root1.right, root2.right)

        return TreeNode(merged_value, left_node, right_node)
```

これも中途半端に破壊的。完全に破壊的にやるなら新しくノードを作らずroot1のノードのvalueに加算していく。root1の側に子が存在しないが、root2の方には存在する場合はroot2のnodeを直接移植する。

```python
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1: return root2
        if not root2: return root1

        queue = deque([(root1, root2)])

        while queue:
            n1, n2 = queue.popleft()
            
            n1.val += n2.val

            if n1.left and n2.left:
                queue.append((n1.left, n2.left))
            elif not n1.left and n2.left:
                n1.left = n2.left

            if n1.right and n2.right:
                queue.append((n1.right, n2.right))
            elif not n1.right and n2.right:
                n1.right = n2.right

        return root1
```

## step3
最初に書いたコードを３回書く。
