class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return (0)
        num_rows = len(grid)
        num_cols = len(grid[0])
        WATER = '0'
        ISLAND = '1'
        visited = set()
        islands = 0
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        def is_land(row, col):
            if not (0<= row < num_rows and 0<= col < num_cols):
                return False
            if (grid[row][col] == WATER):
                return False
            return True

        for r in range(num_rows):
            for c in range(num_cols):
                if (grid[r][c] == WATER):
                    continue
                if ((r, c) in visited):
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
        return (islands)
