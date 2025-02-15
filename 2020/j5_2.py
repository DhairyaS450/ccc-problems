# Performing slightly better than recursive approach, but still only getting 13/15

from collections import deque

# Read input
M = int(input())
N = int(input())
grid = [list(map(int, input().split())) for _ in range(M)]

# Cache for factor pairs
factor_cache = {}

def get_factor_pairs(num):
    """Get all the factor pairs (x, y) for a number that is within the grid"""
    if num in factor_cache:
        return factor_cache[num]
    
    factors = []
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            x, y = i, num // i
            if x <= M and y <= N:
                factors.append((x, y))
            if x != y and y <= M and x <= N:
                factors.append((y, x))
    factor_cache[num] = factors
    return factors

def bfs():
    """BFS to check if we can reach (M, N) from (1, 1)"""
    queue = deque([(1, 1)]) # Start from top-left
    visited = set([(1, 1)]) # Track visited cells

    while queue:
        x, y = queue.popleft()

        # If we reached the bottom-right, return True
        if x == M and y == N:
            return "yes"
        
        num = grid[x - 1][y - 1] # Convert to 0-based indexing
        for nx, ny in get_factor_pairs(num):
            if (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny))

    return "no"

print(bfs())