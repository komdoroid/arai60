## step1
- 文字列をループして初めて出てきた文字は、文字をkeyindexをvalueとして辞書に格納。
- 出現2回目以降の文字はindexを-1に変更
上記の方針でコードを作成する。

### 計算量について
- len(s)ループする
- s in dictはO(1)
- len(s)をもう一度ループしてindex > 0を探す
時間計算量：O(n)
空間計算量：O(n)

### コード
```python
class Solution:
    def firstUniqChar(self, s: str) -> int:
        ch_to_index = {}

        for i in range(len(s)):
            if s[i] in ch_to_index:
                ch_to_index[s[i]] = -1
                continue
            ch_to_index[s[i]] = i
        
        for index in ch_to_index.values():
            if index < 0:
                continue
            return index
        return -1
```

## step2
### コード1
- 1つ目のループはif-elseでも書くことができる
- 2つ目のループはcontinueがいらない
```python
class Solution:
    def firstUniqChar(self, s: str) -> int:
        ch_to_index = {}

        for i in range(len(s)):
            if s[i] in ch_to_index:
                ch_to_index[s[i]] = -1
            else:
                ch_to_index[s[i]] = i

        for index in ch_to_index.values():
            if index >= 0:
                return index
        return -1
```

### コード2
重複を確認するのではなく、出現回数などを見る場合はカウントが必要。
今回の場合は2回出た時点で判断できるので、出現回数のカウントは不要。
```python
class Solution:
    def firstUniqChar(self, s: str) -> int:
        ch_to_count= {}

        for i, ch in enumerate(s):
            if ch in ch_to_count:
                cnt, idx = ch_to_count[ch]
                ch_to_count[ch] = (cnt + 1, idx)
                continue
            ch_to_count[ch] = (1, i)

        for cnt, idx in ch_to_count.values():
            if cnt == 1:
                return idx
        return -1
```
### コード3
next()を使って書くこともできた。最初の要素を返すことが明確になる。
```python
return next((idx for idx in ch_to_index.values() if idx != -1), -1)
```

## step3 
3回間違えずにコードを書く