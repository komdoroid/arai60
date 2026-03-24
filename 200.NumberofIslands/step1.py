class Solution:
     def numIslands(self, grid: List[List[str]]) -> int:
         rows = len(grid)
         colums = len(grid[0])
         islands = 0
         stack = deque((0, 0))
         for i in range(rows):
             for j in range(colums):
                 if grid[i, j] == '1':
