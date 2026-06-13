# 127.WordLadder
## なにを考えて解いたか
`beginWord`から`endWord`までの最短経路を考える問題なので、BFSを使って解く。
とりあえずロジックを以下の順番で考えてみる。

1. 探索の開始
2. 次の遷移先
3. 遷移先が妥当かチェック
4. 探索の終了

### 探索の開始
`wordList`が2つ以上あること

### 次の遷移先
1文字を除いて一致していること

### 遷移先が妥当かどうかのチェック
すでに通過した文字列ではないこと

### 探索の終了
現在の文字列が`endWord`と1文字違いなら`words`を1増やして終了。

---

## step1

しばらく考えたが解けなさそうだったので、解説を確認。
認識ずれをチェックして、見なくてもかけるまで練習。

```py
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)

        if endWord not in word_set:
            return 0

        queue = deque([(beginWord, 1)])
        visited = {beginWord}

        while queue:
            current_word, steps = queue.popleft()
            if current_word == endWord:
                return steps
            for i in range(len(current_word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    if c == current_word[i]:
                        continue
                    next_word = current_word[:i] + c + current_word[i+1:]
                    if next_word in word_set and next_word not in visited:
                        visited.add(next_word)
                        queue.append((next_word, steps + 1))
        return 0
``` 

### 探索の開始
`endWord`が与えられた`wordSet`に存在することだけ確認して、`biginWord`から開始する。

### 次の遷移先
`current_word`と1文字違いかつ、`wordList`に存在する文字列。

### 遷移先の妥当性チェック
`visited`に含まれないこと、`wordList`に含まれること

### 終了条件
`current_word`が`endWord`と一致すること

### 計算量
時間計算量：O(n * word_len * 26)
空間計算量：O(n * word_len)

## step2
他の人のコードや、レビューコメントを見てみる。
visitedは今回の問題的には、変数名として適切でない感じがしたので、used_wordsに変更

## step3
3回何も見ずに書いてみる
