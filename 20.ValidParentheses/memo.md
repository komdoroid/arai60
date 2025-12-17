## step1
### 問題の理解
- `(`,`)`,`{`,`}`,`[`,`]`で構成される文字列がある。すべての括弧が正しい組み合わせ、正しい順番で閉じられるかを判定する。

### 何を考えて解いたか
- スタックの問題であることを"https://1kohei1.com/leetcode/"から知ってしまっている
- 開き括弧の時スタックに入れて、閉じ括弧の時取り出す。
- 閉じ括弧の時に対応する開き括弧が取り出されれば、OK
- 最終的にスタックは空になる
- それ以外の方法は思いつかない
- stackの操作についてちゃんとわかっていないので調べる(https://docs.python.org/ja/3/library/collections.html#collections.deque)

```py
class Solution:
    def isValid(self, s: str) -> bool:
        stack_list = []

        for ch in s:
            if ch is '(' or ch is '{' or ch is '[':
                stack_list.append(ch)
            elif not stack_list:
                return False
            elif ch is ')':
                bracket = stack_list.pop()
                if bracket != '(':
                    return False
            elif ch is '}':
                bracket = stack_list.pop()
                if bracket != '{':
                    return False
            elif ch is ']':
                bracket = stack_list.pop()
                if bracket != '[':
                    return False
        
        if len(stack_list) != 0:
            return False
        return True
```

## step2
### 他の人のコードを読んで
<https://github.com/Yuto729/LeetCode_arai60/pull/12>
- open-close braketsを辞書で管理する方法。
- step1の書き方だと、括弧の種類が増える毎にコードが長くなる。
- 1対1で対応している場合はこの書き方のほうが良さそう。
- 1対多や、多対多で対応していてもkey,vlueをリストにすれば行けそうかな？
- stackにdequeを使う理由はなんだろう？リストとdequeそれぞれの違いについては以下に記載がある。https://docs.python.org/ja/3/library/collections.html#collections.deque)

```py
class Solution:
    def isValid(self, s: str) -> bool:
        open_brackets = deque()
        open_to_close = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }

        for ch in s:
            if ch in open_to_close:
                open_brackets.append(ch)
            
            elif ch in open_to_close.values():
                if not open_brackets or open_to_close[open_brackets.pop()] != ch:
                    return False
        
        if len(open_brackets) != 0:
            return False
        return True
```

<https://github.com/bumbuboon/Leetcode/pull/7#discussion_r1817837783>
> スタックの底に番兵を置いておくのも一応手としてはあります。

- stackが空になるのを確認する必要がなくなる
```py
class Solution:
    def isValid(self, s: str) -> bool:
        open_brackets = deque('0')
        open_to_close = {
            '(' : ')',
            '{' : '}',
            '[' : ']',
            '0' : ''
        }

        for ch in s:
            if ch in open_to_close:
                open_brackets.append(ch)
            else:
                if open_to_close[open_brackets.pop()] != ch:
                    return False
        
        if len(open_brackets) != 1:
            return False
        return True
```

<https://github.com/colorbox/leetcode/pull/4#pullrequestreview-1929977997>
> チョムスキー階層、type-2、文脈自由文法、プッシュダウンオートマトンですね。

- 言語学での分類方法。初めて聞いたが面白い

<https://github.com/rm3as/code_interview/pull/4#discussion_r1563811298>
> 問題文で、()[]{} 以外が来ないことが保証されているようですが、とはいえ、{"(": ")"} の方向の対応にしたほうがいいかもしれません。pair[c] に閉じカッコ以外が入ると例外投げるので。

- 深く考えられていなかったので、意図しない値が入力される場合の挙動も考える。今回のコードでは辞書に含まれない文字は処理されない。

<https://github.com/yus-yus/leetcode/pull/6#discussion_r1944970090>
> 個人的には副作用のある式を条件のところにあまり書きたくないですね。

## step3
step2-2で間違えずに3回書く
