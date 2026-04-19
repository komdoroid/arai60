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

## step2
### 他の人のコードを読んでみる
https://github.com/atmaxstar/coding_practice/pull/2/changes#diff-5ee6c34c8e15002eacc92ba08eea400f87d1753f8dd6eead63e6ea3c96bd967cR149:~:text=max_area%20%3D%20max(max_area%2C%20get_area_starting_from(i%2C%20j))
```python
if aria > max_area:
    max_area = (max_area, area)
```
この部分は１行で書けるので修正。
```python
max_area = max(max_area, area)
```

面積計算部分を関数として切り出せば、max_areaとの比較まで１行で実施できるので関数化する。
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
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        def can_visit(row, col) -> bool:
            if not (0 <= row < num_rows and 0 <= col< num_cols):
                return False
            if (grid[row][col] == WATER):
                return False
            if ((row, col) in visited):
                return False
            return True
        
        def calc_area(row, col) -> int:
            visited.add((row, col))
            stack = [(row, col)]

            area = 1
            while stack:
                y, x = stack.pop()
                for dy, dx in directions:
                    next_y = y + dy
                    next_x = x + dx
                    if not can_visit(next_y, next_x):
                        continue
                    visited.add((next_y, next_x))
                    stack.append((next_y, next_x))
                    area += 1
            return area
        
        for row in range(num_rows):
            for col in range(num_cols):
                if not can_visit(row, col):
                    continue
                max_area = max(max_area, calc_area(row, col))
        return max_area
```

## step3
この状態で３回書く
