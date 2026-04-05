class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return (0)

        num_rows = len(grid);
        num_columns = len(grid[0]);
        islands = 0
        visited = set()
        WATER = '0'
        ISLAND = '1'
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

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
                    x, y = stack.pop
                    for dr, dc in directions:
                        neighbor_x = x + dr
                        neighbor_y = y + dc

                        if not (0 <= neighbor_x < num_rows and 0 <= neighbor_y < num_columns):
                            continue
                        if (neighbor_x, neighbor_y) in visited:
                            continue
                        if grid[neighbor_x][neighbor_y] == WATER:
                            continue
                        stack.append((neighbor_x, neighbor_y))
                        visited.add((neighbor_x, neighbor_y))
        return (islands)
