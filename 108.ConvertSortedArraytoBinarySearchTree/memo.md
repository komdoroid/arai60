# 108.ConvertSortedArraytoBinarySearchTree

## 何を考えて解いたか
'height-balanced' binary search treeなので平衡木を作成する。

実装方法としてはリストの中央値をノードの値として、中央値までの前半後半それぞれについて再帰的に同じ動作を行えば完成する。

## step1
最初に考えた通り、中央値をノードのvalに設定するようにして実装。

```python
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        median = len(nums) // 2
        node = TreeNode(
                nums[median],
                self.sortedArrayToBST(nums[:median]),
                self.sortedArrayToBST(nums[median + 1:])
                )
        return node
```

### 時間計算量
- 再帰の深さは毎回リストを半分にするのでO(logN)
- リストのスライスはリストのコピーを作成するのでO(N)
結果O(NlogN)

### 空間計算量
ノードをNこ作成するので、O(N)

計算量的にもう少し効率の良いやり方がありそう。


## step2
スライスを使わずに、２つのポインタを使用した実装
```python
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        def build_tree(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None
            mid = (left + right) // 2
            node = TreeNode(nums[mid])

            node.left = build_tree(left, mid - 1)
            node.right = build_tree(mid + 1, right)

            return node

        return build_tree(0, len(nums) - 1)
```

他の人のコードを参考にしてみる。
https://github.com/MA-yo-TA/leetcode/pull/24

ループを使った実装
```python
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        root = TreeNode()
        stack = [(0, len(nums) - 1, root)]

        while stack:
            left, right, node = stack.pop()
            mid = (left + right) // 2
            node.val = nums[mid]
            if left < mid:
                node.left = TreeNode()
                stack.append((left, mid - 1, node.left))
            if mid < right:
                node.right= TreeNode()
                stack.append((mid + 1, right, node.right))

        return root
```

## step3
ループでの実装に苦戦したのでループで書いてみる
