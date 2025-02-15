from collections import deque

def main():
    # Read the number of pages
    N = int(input().strip())
    
    # Build the graph: pages are 1-indexed.
    # We'll use a list of lists where graph[i] holds the pages reachable from page i.
    graph = [[] for _ in range(N + 1)]
    
    for i in range(1, N + 1):
        # Read the entire line and split it into tokens
        tokens = input().split()
        m = int(tokens[0])
        if m > 0:
            # Convert the rest of the tokens to integers representing pages
            graph[i] = list(map(int, tokens[1:]))
        # If m == 0, graph[i] remains an empty list (an ending page)
    
    # Set up BFS: we'll store (page, steps) in our queue.
    visited = [False] * (N + 1)
    queue = deque([(1, 1)])  # Starting at page 1, count it as 1 page read.
    visited[1] = True
    shortest = None  # Will hold the shortest path to an ending page
    
    while queue:
        page, steps = queue.popleft()
        
        # If this page has no options, it's an ending page.
        if not graph[page]:
            # Because we're using BFS, the first ending page we see has the shortest path.
            if shortest is None:
                shortest = steps
        
        # Process all reachable pages from the current page.
        for next_page in graph[page]:
            if not visited[next_page]:
                visited[next_page] = True
                queue.append((next_page, steps + 1))
    
    # Check if every page was reached (pages 1 through N).
    all_reachable = all(visited[1:])
    
    # Print results: "Y" if all pages are reachable, otherwise "N".
    print("Y" if all_reachable else "N")
    print(shortest)

if __name__ == '__main__':
    main()
