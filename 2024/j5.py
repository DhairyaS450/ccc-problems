import sys
sys.setrecursionlimit(100000)

rows = int(input())
cols = int(input())
# print('Rows:', rows)
# print('Columns:', cols)
grid = [list(input()) for _ in range(rows)]
starting_row = int(input())
starting_col = int(input())
total = 0
visited = set()

def collect(x, y):
    global total
    if x < 0 or y < 0 or x >= rows or y >= cols:
        return
    tile = grid[x][y]
    if tile == "*":
        return

    if tile == 'S': total += 1
    elif tile == 'M': total += 5
    elif tile == 'L': total += 10
    grid[x][y] = '*'
    
    collect(x + 1, y)
    collect(x - 1, y)
    collect(x, y + 1)
    collect(x, y - 1)

collect(starting_row, starting_col)

print(total)