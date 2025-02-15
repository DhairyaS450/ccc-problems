# This solution hits TLE and only scores 13/15, seems that recursion is too slow for this problem
import sys
sys.setrecursionlimit(100000)

M = int(input())
N = int(input())
grid = [list(map(int, input().split())) for _ in range(M)]

def get_factor_pairs(num):
    factors = []
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            x, y = i, num//i
            if x <= M and y <= N:
                factors.append((x, y))
            if y <= M and x <= N:
                factors.append((y, x))
            
    return factors

# print(grid)
# print(get_factor_pairs(12))

is_exitable = False
# Current x and current y are 1-based
def find_exit(current_x, current_y, visited: set):
    global is_exitable
    if (current_x, current_y) in visited:
        return
    if current_x == M and current_y == N:
        is_exitable = True
        return True
    
    visited.add((current_x, current_y))
    num = grid[current_x - 1][current_y - 1] # Make it 0 based

    next_places = get_factor_pairs(num)
    for place in next_places:
        find_exit(place[0], place[1], visited)

find_exit(1, 1, set())

if is_exitable:
    print('yes')
else:
    print('no')