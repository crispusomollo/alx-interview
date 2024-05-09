def island_perimeter(grid):
    perimeter = 0
    rows, cols = len(grid), len(grid[0])

    # Iterate through each cell in the grid
    for i in range(rows):
        for j in range(cols):
            # Check if the current cell is land
            if grid[i][j] == 1:
                # Check each neighbor of the current cell
                for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    ni, nj = i + dx, j + dy
                    # Check if the neighbor is out of bounds or water
                    if ni < 0 or nj < 0 or ni >= rows or nj >= cols or grid[ni][nj] == 0:
                        perimeter += 1  # Increment perimeter for each water cell neighboring land
    return perimeter

# Example usage:
grid = [
    [0, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 0]
]

print(island_perimeter(grid))  # Output: 16

