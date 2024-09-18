import sys
# increase the number of times recursion can occur to pass the last set of cases
sys.setrecursionlimit(100000)

#get input number of rows, columns, grid and starting position
rows = int(input())
cols = int(input())
grid = [list(input()) for _ in range(rows)]
starting_row = int(input())
starting_col = int(input())

#keep track of the total value of pumpkins
total = 0

#recursive function to go through the grid and collect all the available pumpkins
def collect(x, y):
    global total
    #make sure current location is within the grid
    if x < 0 or y < 0 or x >= rows or y >= cols:
        return
    tile = grid[x][y]
    if tile == "*":
        return

    if tile == 'S': total += 1
    elif tile == 'M': total += 5
    elif tile == 'L': total += 10
    #once the tile is collected, set it to a hay bale so it cannot be collected again
    grid[x][y] = '*'

    #try going down
    collect(x + 1, y)
    #try going up
    collect(x - 1, y)
    #try going right
    collect(x, y + 1)
    #try going left
    collect(x, y - 1)

#start collecting from the starting position
collect(starting_row, starting_col)

print(total)
