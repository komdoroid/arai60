## step1 
- "@"より前の"."を削除する
- "@"より前の"+"から"@"までを削除する
- この状態で固有の要素を見つける
上記の方針で考えたが、具体的な実装ができず手が止まったため答えを見る。

- https://leetcode.com/problems/unique-email-addresses/solutions/261959/easy-understanding-python-solution-44ms-uy8p8/
    - この回答を参考にhashmapを使ってみる

### コード
```python
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        def parse(email):
            local, domain = email.split('@')
            local = local.split('+')[0].replace('.', "")
            return f"{local}@{domain}"
        
        seen = {}

        for email in emails:
            normalized = parse(email)
            if normalized not in seen:
                seen[normalized] = True
        return len(seen)
```

### 計算量
- emails.length = n
- email[i].length = m
とした場合
- 時間計算量 : O(n * m)
- 空間計算量 : O(n * m)

## step2 
- https://discord.com/channels/1084280443945353267/1418089977585336390/1429275622773096449
> 関数型的な見え方は並列化しやすかったり色々と利点はあるのですが、中間状態が大きくなったり変形しにくい状態になったりするので、たまに一回そうしないとして考えてみるというのはしますね。

関数を使わないで書いてみることを考える。

### コード
```python
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        normalized_to_seen = {}
        for email in emails:
            local, domain = email.split('@')
            local = local.split('+')[0].replace('.', "")
            normalized = local + '@' + domain
            normalized_to_seen[normalized] = True

        return len(normalized_to_seen)            
```

関数を使用した方が読みやすいと感じた、保守もしやすそう。
重複はsetで消せるのでsetを使ってstep1を修正する。
### コード2-2
```python
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        def normalize(email):
            local, domain = email.split('@')
            local = local.split('+')[0].replace('.', "")
            return f"{local}@{domain}"

        normalized_emails = {normalize(email) for email in emails}
        return len(normalized_emails)      
```

### 計算量
step1と同様
- 時間計算量 : O(n * m)
- 空間計算量 : O(n * m)

## step3
間違えずに3回書く