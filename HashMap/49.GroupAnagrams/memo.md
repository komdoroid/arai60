## わからなかったこと・質問
## step1
- 全ての場合を列挙して比較することは避ける方針で考える。
- `strs`の要素をset型のオブジェクトに変換して、共通の文字を使っていることで判定しようかと考えたが、重複が考慮されないのでやめる。

- わからなかったのでアナグラムについて少し調べてみると、文字列をアルファベット順にソートする方法があったので参考にして実装する。
https://qiita.com/arie0703/items/1291f36dccf29f3300da
### 実装結果
```python
class Solution(object):
    def groupAnagrams(self, strs):
        sorted_to_word = {}

        for word in strs:
            key = ''.join(sorted(word))
            if key not in sorted_to_word.keys():
                sorted_to_word[key] = [word]
            else:
                sorted_to_word[key].append(word)
        return list(sorted_to_word.values())
```

---

## step2
- 計算量が概算できないので調べる: https://leetcode.com/problems/group-anagrams/solutions/4683832/beats-99-users-cjavapythonjavascript-2-a-ihgq/?envType=problem-list-v2&envId=xo2bgr0r
- `s in x`は計算量がO(n)、sortはO(nlog(n))になるようなので、上記のコードだと
    - `strs.length = n`
    - `strs[i].length = n`
の場合O(n^2 logn)の計算量になる。
- 今回の条件は
    - `1 <= strs.length <= 10^4`
    - `0 <= strs[i].length <= 100`
    なのでmax:10^6程度
- 今回python.orgが公開していた計算量をそのまま参考にした(https://wiki.python.org/moin/TimeComplexity)
- 自分でもCPythonを調べてみる
- 計算量をふまえて、より良い実装がないか調べてみる
- 各文字列に対して、a~zが何回出てくるかを数える方針での実装があった。(https://leetcode.com/problems/group-anagrams/solutions/4683832/beats-99-users-cjavapythonjavascript-2-a-ihgq/?envType=problem-list-v2&envId=xo2bgr0r)
- この実装方法ならsortがない分早い。
- strs[i].lengthが十分大きくなればstep1の方法と実行速度に差はでなさそうだが、今回条件が`0 <= strs[i].length <= 100`のため、a~zをカウントする方法で実装する

### 実装結果
```python
class Solution(object):
    def groupAnagrams(self, strs):
        count_to_word = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for chr in word:
                count[ord(chr) - ord('a')] += 1
            key = tuple(count)
            count_to_word[key].append(word)
        return list(count_to_word.values())
```

----

## step3
1回目:3m
2回目:2.5m
3回目:3m