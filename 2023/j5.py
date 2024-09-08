word = input()
rows = int(input())
cols = int(input())
grid = []
for i in range(rows):
    grid.append(input().split())
    
count = 0
def dfs(d, x, y, dx, dy, turned):
    global count
    if x < 0 or x >= rows or y < 0 or y >= cols: return
    if grid[x][y] != word[d]: return
    if d == len(word) - 1:
        count+=1
        return
    dfs(d+1, x+dx, y+dy, dx, dy, turned)

    if d >= 1 and not turned:
        dfs(d+1, x-dy, y+dx, -dy, dx, True)
        dfs(d+1, x+dy, y-dx, dy, -dx, True)

for x in range(rows):
    for y in range(cols):
        if grid[x][y] == word[0]:
            dfs(0, x, y, -1, -1, False)
            dfs(0, x, y, -1, 0, False)
            dfs(0, x, y, -1, 1, False)
            dfs(0, x, y, 0, -1, False)
            dfs(0, x, y, 0, 1, False)
            dfs(0, x, y, 1, -1, False)
            dfs(0, x, y, 1, 0, False)
            dfs(0, x, y, 1, 1, False)

print(count)