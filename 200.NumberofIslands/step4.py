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

        def explore_island(row, col):
            visited.add((row, col))
            stack = [(row, col)]

            while  stack:
                x, y = stack.pop()
                for dr, dc in direction:
                    nx = x + dr
                    ny = y + dc

                    if (nx, ny) in visited:
                        continue
                    if not is_land(nx, ny):
                        continue
                    stack.append((nx, ny))
                    visited.add((nx, ny))


        for r in range(num_rows):
            for c in range(num_columns):
                if grid[r][c] == WATER:
                    continue
                if (r, c) in visited:
                    continue
                visited.add((r, c))
                stack = [(r, c)]

                explore_island(r, c)
                islands += 1
        
        return islands
