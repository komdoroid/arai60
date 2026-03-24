class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return (0)

        row_nums = len(grid)
        col_nums = len(grid[0])
        islands = 0
        visited = set()
        WATER = '0'
        ISLAND = '1'
        
        def is_lnad(row, col):
            if not (0 <= row < row_nums and 0 <= col < col_nums):
                return (False)
            if grid[row][col] == WATER:
                return (False)
            return (True)

        for r in range (row_nums):
            for c in range (col_nums):
                if grid[r][c] == WATER:
                    continue
                if grid[r][c] in visited:
                    continue
                islands += 1
                stack = [(r, c)]
                visited.add((r, c))

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
        return (islands)
