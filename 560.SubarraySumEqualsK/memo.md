## step1
### 問題の理解
- 配列`nums`と整数`k`を受け取り、要素の合計がkとなるようなsubarrayの個数を求める
- subarrayとは、配列に含まれる空でない連続した要素のこと
### 何を考えたか
- nums全体をループして、i番目の要素からi+1, i+2...番目の要素を足し合わせてsum == kとなったらcountを1増やす。
- この方法だとn = num.lengthの場合時間計算量がO(n^2)になる。空間計算量はO(1)。
- nums.length <= 2 * 10^4なので時間がかかりすぎる -> 保留
- 他の実装が思いつかない
- 書いてみるがTLE
```python
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0

        for i in range(len(nums)):
            subarray_sum = 0
            for j in range(i, len(nums)):
                subarray_sum += nums[j]
                if subarray_sum == k:
                    count += 1
                
        return count
```
### 実装方法調査
- 他の参加者のPRを参考
    - https://github.com/Kaichi-Irie/leetcode-python/pull/26
    - https://github.com/t9a-dev/LeetCode_arai60/pull/6
    - https://github.com/docto-rin/leetcode/pull/16
- 累積和を利用することで実現可能
1. numsをループしてある時点までの累積和(prefix_sum)を保持しておく
2. 配列nums[l, r]の和は`prefix_sum[r] - prefix_sum[l-1]`
これがkに等しい条件は`prefix_sum[r] - prefix_sum[l-1] = k`
3. 変形すると`prefix_sum[l-1] = prefix_sum[r] - k`。

つまり、今の累積和からkを引いた値が過去に累積和として出てきた回数を数えることで、今の位置を右端とする和がkのsubarrayの個数がわかる

- 数式を見ればその通りなのだが、個人的には直感的にわかりにくい
- subarrayの合計 = kを探す -> 現在の累積和 - ある時点の累積和 = kになればよい -> 現在の累積和 - k = ある時点の累積和 となるような場合を数える -> すべての要素に対して実行

```python
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        prefix_to_count = defaultdict(int)

        prefix_to_count[0] = 1
        for num in nums:
            prefix_sum += num
            count += prefix_to_count[prefix_sum - k]
            prefix_to_count[prefix_sum] += 1
        return count
```
- `prefix_to_count[0] = 1`の部分がすぐに理解できず少し悩んだ。
- 時間計算量：numsに対して1回ループを実行するのでO(n)
- 空間計算量：O(n)
## step2
### 他の参加者へのコメントをみた感想
- https://discord.com/channels/1084280443945353267/1195700948786491403/1253638682829783061
    - この流れは参考になった。わかる形で実装を行って、そこから自明な変形を繰り返していくプロセスは取り入れられるようにしたい。
    - 累積和を使う発想は問題を見て、自分で思いつく必要がある？
- https://github.com/docto-rin/leetcode/pull/16/commits/84080fc16480525f97ecf5bb8c8681f20cbcbdfe#:~:text=%23operator%2Dprecedence-,%2D,-if%20current_sum%20%2D
    - 確かに分岐を追加した方が良い
- https://github.com/katataku/leetcode/pull/15/commits/7728d62d9ce2b77372315886a9bbcd25dfb0cd32#r1903868949
    - defaultdictを使わずに実装してみる
```python
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        prefix_to_count = {0: 1}

        for num in nums:
            prefix_sum += num
            if prefix_sum - k  in prefix_to_count:
                count += prefix_to_count[prefix_sum - k]
            if prefix_sum in prefix_to_count:
                prefix_to_count[prefix_sum] += 1
            else:
                prefix_to_count[prefix_sum] = 1
        return count
```
以下の部分は`count += prefix_to_count.get(prefix_sum - k, 0)`と書くことができる。
```python
if prefix_sum - k  in prefix_to_count:
    count += prefix_to_count[prefix_sum - k]
```
