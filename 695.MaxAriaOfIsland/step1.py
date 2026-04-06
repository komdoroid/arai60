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
