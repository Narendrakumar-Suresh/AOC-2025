with open("./day4/input.txt", "r") as file:
    lines = file.readlines()

grid = [list(line.strip()) for line in lines]

directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

rows = len(grid)
cols = len(grid[0]) if rows > 0 else 0

def count_neighbors(grid, r, c):
    count = 0
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '@':
            count += 1
    return count

total_removed = 0

while True:
    to_remove = []
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '@' and count_neighbors(grid, r, c) < 4:
                to_remove.append((r, c))
    
    if not to_remove:
        break
    
    for r, c in to_remove:
        grid[r][c] = '.'
    
    total_removed += len(to_remove)

print(f"\nTotal rolls removed: {total_removed}")