## step1
以下の方針で進める
nums1の要素をループして、各要素がnum2に含まれているか調べる。
含まれていた場合は、リストの場合だと重複が発生する可能性があるので辞書に格納。
実行完了後、辞書のkeyを結果として返す。

### 計算量について
`for`と`nums[i] in nums2`を使用しているのでnums1.length * nums2.length

### コード
```python
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num_to_index = {}
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                num_to_index[nums1[i]] = i
        return list(num_to_index)
```

## step2
1. `nums1[i] in nums2`を使うことで、計算量が増える
2. 辞書のvalueとして無意味な値を入れている
↑の2点が気になったので、別のコードを検討。
`set`を使用すればかなりシンプルに無駄なく書ける。
この場合のデメリットを考えてみたが、思いつかなかったので`set`を使用する。

### コード
```python
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set_nums1 = set(nums1)
        set_nums2 = set(nums2)
        return list(set_nums)
```

## step3
1回目: 1m
2回目: 1m
3回目: 1m
