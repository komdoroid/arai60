# 111. Minimus Depth of Binary Tree

## 何を考えて解いたか
BFSで解いて、最初に次の `self.left` と `self.right` 両方が `Null`になるものを見つけたらそこまでの深さを返せば良いのでは
`is None`は明示するように。

## step1

```python
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        node_and_depth = deque([(root, 1)])
        
        while node_and_depth:
            node, current_depth = node_and_depth.popleft()

            if node.left is None and node.right is None:
                return (current_depth)
            if node.left is not None:
                node_and_depth.append((node.left, current_depth + 1))
            if node.right is not None:
                node_and_depth.append((node.right, current_depth + 1))
```

`104. Maximum Depth of Binary Tree` を参考にしながら、書いた。

## step2
再帰を使って書く。
木構造のleaf nodeを正しく理解していなかった。
どちらか一方でも子ノードがいる場合はleaf nodeではない。

```python
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        left_depth = self.minDepth(root.left)
        right_depth = self.minDepth(root.right)

        return min(left_depth, right_depth) + 1
```

正しく、leaf nodeであることを確認しているのが以下のコード

```python
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        left_depth = self.minDepth(root.left)
        right_depth = self.minDepth(root.right)
        if left_depth == 0:
            return right_depth + 1
        if right_depth == 0:
            return left_depth + 1

        return min(left_depth, right_depth) + 1
```

## step3
ループと再帰を両方書き直してみる。
