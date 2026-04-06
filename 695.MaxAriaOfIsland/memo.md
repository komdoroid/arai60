## 何を考えて解いたか
200. Number of Islandsと似た流れで解ける気がする。
grid[0][0]からgrid[maxrow][maxcol]までをチェックして、`1`があれば訪問済みか確認し幅優先探索を開始する。

前回考えていた、探索の流れを整理する。
1. 探索の開始: 現在の場所が`1`であること
2. 現在の状態からの遷移先: 現在の場所から上下左右1マス
3. 重複確認: visitedに同じ値が格納されていない事
4. 終了条件: 移動可能な陸地の探索が全て終了（stack)が空

Number of Islandsと異なるのは島の数を数えるのか、島の最大面積を調べるのか。

## step1

```python
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        num_rows = len(grid)
        num_cols = len(grid[0])
        max_area = 0
        visited = set()
        WATER = 0
        LAND = 1
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] != LAND:
                    continue
                if (row, col) in visited:
                    continue
                stack = [(row, col)]
                visited.add((row, col))

                area = 1
                while stack:
                    y, x = stack.pop()
                    for dy, dx in directions:
                        next_y = y + dy
                        next_x = x + dx
                        if not (0 <= next_y < num_rows and 0 <= next_x < num_cols):
                            continue
                        if grid[next_y][next_x] == WATER:
                            continue
                        if (next_y, next_x) in visited:
                            continue
                        stack.append((next_y, next_x))
                        visited.add((next_y, next_x))
                        area += 1
                if area > max_area:
                    max_area = area
        return max_area
```

## 計算量の検討
### 時間計算量
外側のループ：row * col
内側のループ：各grid[row][col]は一度しかstackに入らないので、最大でもrow * col
O(row * col)

### 空間計算量
stackとvisitedが保持する可能性のある最大値はどちらもrow * col個
O(row * col)