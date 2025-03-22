from collections import deque

# graph = {
#     1: [2, 3],
#     2: [4, 5],
#     3: [6],
#     4: [],
#     5: [],
#     6: []
# }

# print("BFS")
# def bfs(graph, start):
#     queue = deque([start])
#     visited = set([start])

#     while queue:
#         node = queue.popleft()
#         print(node, end=' ')
#         for neighbor in graph[node]:
#             if neighbor not in visited:
#                 visited.add(neighbor)
#                 queue.append(neighbor)

# # Example usage
# bfs(graph, 1)

# print("\nDFS")
# def dfs(graph, node, visited):
#     if node in visited:
#         return
#     visited.add(node)
#     print(node, end=" ")  # Process the node
#     for neighbor in graph[node]:
#         dfs(graph, neighbor, visited)

# # Example usage
# visited = set()
# dfs(graph, 1, visited)

# graph = {
#     1: [2, 5],
#     2: [4, 3],
#     3: [],
#     4: [5, 8, 10],
#     5: [6, 7],
#     6: [8],
#     7: [],
#     8: [10],
#     10: []
# }

# # Find shortest path from 1-10 using BFS
# def bfs(graph, start, target):
#     queue = deque([(start, 0)])
#     visited = set([start])
#     parent = {start: None } # Track parent nodes

#     while queue:
#         node, dist = queue.popleft()
#         if node == target:
#             # Reconstruct the path from target back to start
#             path = []
#             while node is not None:
#                 path.append(node)
#                 node = parent[node]
#             path.reverse()
#             return dist, path
        
#         neighbors = graph[node]
#         for neighbor in neighbors:
#             if neighbor not in visited:
#                 visited.add(neighbor)
#                 parent[neighbor] = node # Store parent to track path
#                 queue.append((neighbor, dist + 1))

#     return -1, []
    
# distance, path = bfs(graph, 1, 10)
# print(f"Shortest distance: {distance}")
# print(f"Path taken: {path}")



grid = [
    [(0,1), (1,0), (1,2)],
    [(0,2), (0,0), (1,1)]
] # Path is (0,0) -> (0,1) -> (1,0) -> (0,2) -> (1,2)
start_x = 0
start_y = 0
target_x = 1
target_y = 2

def bfs(grid, start_x, start_y, target_x, target_y):
    queue = deque([(start_x, start_y, 0)])
    visited = set([(start_x, start_y)])

    while queue:
        x, y, dist = queue.popleft()
        if x == target_x and y == target_y:
            return dist
        
        print(x, y, grid[x][y])
        next_x, next_y = grid[x][y]
        if (next_x, next_y) not in visited:
            queue.append((next_x, next_y, dist+1))

    return -1

print(bfs(grid, start_x, start_y, target_x, target_y))

