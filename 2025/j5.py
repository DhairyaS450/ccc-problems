def min_connecting_path_cost_opt(R, C, M):
    # Initialize the first row (inlined cost computation).
    prev = [((0 * C + c) % M) + 1 for c in range(C)]
    
    for r in range(1, R):
        curr = [0] * C
        base = r * C  # Compute once per row.
        for c in range(C):
            # Inline tile cost calculation.
            cost_here = ((base + c) % M) + 1
            
            # Unroll the three allowed moves explicitly.
            best_prev = prev[c]
            if c > 0:
                if prev[c - 1] < best_prev:
                    best_prev = prev[c - 1]
            if c < C - 1:
                if prev[c + 1] < best_prev:
                    best_prev = prev[c + 1]
                    
            curr[c] = cost_here + best_prev
        prev = curr  # Update the DP row.
    
    return min(prev)

# Example usage:
R = int(input())
C = int(input())
M = int(input())
print(min_connecting_path_cost_opt(R, C, M))
