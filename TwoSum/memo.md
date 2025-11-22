## 質問・わからなかったこと
1. 
```python
def twoSum(self, nums: List[int], target: int) -> List[int]:
```
を明示的に書くべきかどうかの感覚がわかりませんでした。
2. 
必ず1つ回答が存在するという条件で、見つからなかった場合の処理が必要かどうかの感覚がわかりませんでした。

## step1
2重ループを避けて、現在の要素と'target'の差が現在の要素より後ろに存在するかを確認する方針で進める。
```python
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in nums[i+1:]:
                return ([i, nums.index(diff)])
```
後ろのindexの取得がうまく処理できなかったため、ポインタを2つ使用して綺麗にできないか考る。しかし上記と同じ問題に悩んで良い実装がわからなかったので無理やり出力を合わせてAccept。
```python
class Solution(object):
    def twoSum(self, nums, target):
        l, r = 0, 0
        while l<len(nums):
            diff = target - nums[l]
            if diff in nums[l+1:]:
                r = l + nums.index(diff) + 1
                return ([l, r])
```

## step2
以下の回答などを参考に、hashmapを使用した方がすっきりしそうだったので修正
https://leetcode.com/problems/two-sum/solutions/2990807/solution-cjavapython-both-brute-force-op-m6er/?envType=problem-list-v2&envId=xo2bgr0r
```python
class Solution(object):
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[nums[i]] = i
```

## step3
3回かけるまで実施。
```python
class Solution(object):
    def twoSum(self, nums, target):
        hashmap = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[nums[i]] = i
```