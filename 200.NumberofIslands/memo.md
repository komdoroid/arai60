## step1
### 何を考えて解いたか
- DFS, BFSをあまり理解していないので調べる。
- DFS : スタックを使う。一つのルートを深く探索する。
- BFS : キューを使う。スタートの位置から近い順に探索する。
- 今回の問題ならどちらが適しているのか考えてみたが、島の形次第なのでは？と思った。
- DFSを使って解いてみる。
- 自力では解けず

```py
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        colums = len(grid[0])
        islands = 0
        stack = deque((0, 0))
        for i in range(rows):
            for j in range(colums):
                if grid[i, j] == '1':
```

### 他の参加者のコードを参考にして解く
以下参考にしたコード
- https://github.com/Yuto729/LeetCode_arai60/pull/22
- https://github.com/Kaichi-Irie/leetcode-python/pull/28

流れを理解しやすくするために関数は使わずに一度書いてみる

### DFSの流れ
他の参加者のコードなどをみて、流れをまとめてみる。
1. 探索の開始
2. 現在の状態からの遷移先
3. 重複探索確認
4. 探索終了条件確認
それぞれ何が条件かを考えると、見通しが良い気がする。

```py
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        num_rows = len(grid)
        num_columns = len(grid[0])
        islands = 0
        visited = set()
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        for r in range(num_rows):
            for c in range(num_columns):
                if grid[r][c] == "0":
                    continue
                if (r, c) in visited:
                    continue
                islands += 1
                visited.add((r, c))
                stack = [(r, c)]

                while stack:
                    x, y = stack.pop()
                    for dr, dc in directions:
                        neighbor_x = x + dr
                        neighbor_y = y + dc

                        if not (0 <= neighbor_x < num_rows and 0 <= neighbor_y < num_columns):
                            continue
                        if (neighbor_x, neighbor_y) in visited:
                            continue
                        if grid[neighbor_x][neighbor_y] == "0":
                            continue
                        
                        stack.append((neighbor_x, neighbor_y))
                        visited.add((neighbor_x, neighbor_y))
        
        return islands
```

### 計算量について
- 外側の2重ループについてO(num_rows * num_colums)
- while内で各マスが登場する回数は高々１回なので、O(num_rows * num_colums)
- directionsのループは定数
- 時間計算量:O(num_rows * num_columns)
- visitedとstackが最大全マス
- 空間計算量:O(num_rows * num_columns)

## step2
### 他の人のコードやコメントを読んで考えたこと
- https://github.com/Yuto729/LeetCode_arai60/pull/22/commits/87c772725c9d702298606e5a1b5e7335525e78cd#r2649008279
参考にして、条件分岐を関数にまとめてみる。また、わかりやすいように島と海に名前を付けるのはいいアイデアだと思ったので参考にする
```py
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        num_rows = len(grid)
        num_columns = len(grid[0])
        islands = 0
        visited = set()
        WATER = "0"
        ISLAND = "1"
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        def is_land(row, column):
            if not (0 <= row < num_rows and 0 <= column < num_columns):
                return False
            if grid[row][column] == WATER:
                return False
            return True

        for r in range(num_rows):
            for c in range(num_columns):
                if grid[r][c] == WATER:
                    continue
                if (r, c) in visited:
                    continue
                islands += 1
                visited.add((r, c))
                stack = [(r, c)]

                while stack:
                    x, y = stack.pop()
                    for dr, dc in directions:
                        neighbor_x = x + dr
                        neighbor_y = y + dc

                        if (neighbor_x, neighbor_y) in visited:
                            continue
                        if not is_land(neighbor_x, neighbor_y):
                            continue
                        
                        stack.append((neighbor_x, neighbor_y))
                        visited.add((neighbor_x, neighbor_y))
        
        return islands
```

### BFSでも解いてみる
- 今回の問題でDFSとBFSでどのような違いがあるのかわからなかった。

```py
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        num_rows = len(grid)
        num_columns = len(grid[0])
        WATER = "0"
        ISLAND = "1"
        visited = set()
        islands = 0
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        for r in range(num_rows):
            for c in range(num_columns):
                if (r, c) in visited:
                    continue
                if grid[r][c] == WATER:
                    continue
                islands += 1
                visited.add((r, c))
                queue = deque([(r, c)])
                while queue:
                    x, y = queue.popleft()
                    for dr, dc in directions:
                        neighbor_x = x + dr
                        neighbor_y = y + dc
                        if not (0 <= neighbor_x < num_rows and 0 <= neighbor_y < num_columns):
                            continue
                        if grid[neighbor_x][neighbor_y] == WATER:
                            continue
                        if (neighbor_x, neighbor_y) in visited:
                            continue
                        queue.append((neighbor_x, neighbor_y))
                        visited.add((neighbor_x, neighbor_y))
        return islands
```
