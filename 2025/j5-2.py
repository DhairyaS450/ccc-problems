from collections import deque

def min_connecting_path(R, C, M):
    # Initialize distance array
    dist = [[float('inf')] * C for _ in range(R)]
    q = deque()
    
    # Seed the top row
    for c in range(C):
        cost = ((0 * C + c) % M) + 1
        dist[0][c] = cost
        q.append((0, c))
    
    # Process the queue
    while q:
        r, c = q.popleft()
        # If we're at the bottom row, no need to explore further
        if r == R - 1:
            continue
        
        # Explore the three possible moves: down-left, down, down-right
        for dc in [-1, 0, 1]:
            nc = c + dc
            if 0 <= nc < C:  # Check bounds
                nr = r + 1
                cost_here = ((nr * C + nc) % M) + 1
                new_cost = dist[r][c] + cost_here
                if new_cost < dist[nr][nc]:
                    dist[nr][nc] = new_cost
                    q.append((nr, nc))
    
    # Return the minimum cost to reach the bottom row
    return min(dist[R-1])

# Example usage (same as your input):
R = int(input())
C = int(input())
M = int(input())
print(min_connecting_path(R, C, M))