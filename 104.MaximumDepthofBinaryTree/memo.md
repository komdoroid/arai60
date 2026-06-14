# 104. Maximum Depth of Binary Tree
## 何を考えて解いたか
### Binary Tree
1つのノードから枝分かれする子のーどが最大でも2つに制限されているツリー構造のデータ型

すべてのノードを探索して一番深いものを求める。
DFSを使用して求められそう。
途中で手が進まず、解説を参照、、、

## step1
再帰を使うことでかなりシンプルに記述できる。`maxDepth`自体がint を返すことになっているので、帰りがけに自分の値を追加して深さを返すことにする。

```py
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return max(left_depth, right_depth) + 1
```

### 計算量
時間計算量：O(n) (要素の数だけ）
空間計算量：O(n)（最悪の場合、n回再帰）

## step2
DFSでの実施を考える。
[参考にした過去参加者のコードと、コメント](ttps://github.com/Kazuuuuuuu-u/arai60/pull/22/changes/6e752c50f715ca9050b694892aae03c2656529c9)

```py
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        node_and_depth = [(root, 1)]
        max_depth = 0

        while node_and_depth:
            node, current_depth = node_and_depth.pop()

            if node:
                max_depth = max(max_depth, current_depth)
                if node.right:
                    node_and_depth.append((node.right, current_depth + 1))
                if node.left:
                    node_and_depth.append((node.left, current_depth + 1))

        return max_depth
```

### 計算量
時間計算量：O(n) (要素の数だけ）
空間計算量：O(n)（最悪の場合、stackにn要素貯まる）
## step3
DFSの書き方がまだなれないのでDFSで3回書く。
