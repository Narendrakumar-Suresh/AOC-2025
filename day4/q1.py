with open("./day4/input.txt", "r") as file:
    lines = file.readlines()

grid = [list(line.strip()) for line in lines]
directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

rows = len(grid)
cols = len(grid[0]) if rows > 0 else 0

accessible_count = 0

for r in range(rows):
    for c in range(cols):
        if grid[r][c] == '@':
            neighbor_count = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '@':
                    neighbor_count += 1
            
            if neighbor_count < 4:
                accessible_count += 1

print(f"Accessible rolls: {accessible_count}")