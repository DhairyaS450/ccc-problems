#!/usr/bin/env python3
import sys

def can_build(L, N, trees):
    # The domain for placing the top-left corner is an M×M grid, where M = N - L + 1.
    M = N - L + 1
    blocked_rects = []
    # For each tree, determine the rectangle of placements that would force the square to cover it.
    for r, c in trees:
        r1 = max(1, r - L + 1)
        r2 = min(r, M)
        c1 = max(1, c - L + 1)
        c2 = min(c, M)
        if r1 <= r2 and c1 <= c2:
            blocked_rects.append((r1, r2, c1, c2))
    
    total = M * M
    # If no rectangle blocks any placement, then the entire domain is free.
    if not blocked_rects:
        return True

    # Coordinate compression: only these boundaries are interesting.
    rows_set = {1, M + 1}
    cols_set = {1, M + 1}
    for r1, r2, c1, c2 in blocked_rects:
        rows_set.add(r1)
        rows_set.add(r2 + 1)
        cols_set.add(c1)
        cols_set.add(c2 + 1)
    
    rows = sorted(rows_set)
    cols = sorted(cols_set)
    
    # Calculate the union area of the blocked rectangles over the compressed grid.
    union_area = 0
    for i in range(len(rows) - 1):
        for j in range(len(cols) - 1):
            # Representative point for the current cell.
            rep_r = rows[i]
            rep_c = cols[j]
            covered = False
            for (rr1, rr2, cc1, cc2) in blocked_rects:
                if rr1 <= rep_r <= rr2 and cc1 <= rep_c <= cc2:
                    covered = True
                    break
            if covered:
                # The area represented by this cell is the product of the cell's width and height.
                area = (rows[i + 1] - rows[i]) * (cols[j + 1] - cols[j])
                union_area += area

    # A valid placement exists if the union of all blocked placements doesn't cover the entire domain.
    return union_area < total

def find_max_pool(N, trees):
    lo, hi, ans = 1, N, 0
    while lo <= hi:
        mid = (lo + hi) // 2
        if can_build(mid, N, trees):
            ans = mid
            lo = mid + 1  # Try a larger pool.
        else:
            hi = mid - 1  # Too big, try a smaller pool.
    return ans

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    N = int(data[0])
    T = int(data[1])
    trees = []
    index = 2
    for _ in range(T):
        r = int(data[index])
        c = int(data[index + 1])
        trees.append((r, c))
        index += 2
    print(find_max_pool(N, trees))

if __name__ == '__main__':
    main()
