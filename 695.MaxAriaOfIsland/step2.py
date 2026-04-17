class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        num_rows = len(grid)
        num_cols = len(grid[0])
        max_area = 0
        visited = set()
        LAND = 1
        WATER = 0
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        for row in range(num_rows):
            for col in range(num_cols):
                if (grid[row][col] == 0):
                    continue
                if ((row, col) in visited):
                    continue
                visited.add((row, col))
                stack = [(row, col)]

                aria = 1
                while stack:
                    y, x = stack.pop()
                    for dy, dx in directions:
                        next_y = y + dy
                        next_x = x + dx
                        if (!(0 <= next_y < num_rows and 0 <= next_x < num_cols)):
                            continue
                        if (grid[next_y][next_x] == 0):
                            continue
                        if ((next_y, next_x) in visited):
                            continue
                        visited.add((next_y, next_x))
                        stack.append((next_y, next_x))
                        aria += 1
                if (max_aria < aria):
                    mas_aria = aria
        return max_aria
