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
