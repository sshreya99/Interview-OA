# intervals in delivery network

def min_connected_zones(a, b, k):
    indices = sorted(range(len(a)), key=lambda i: a[i])
    intervals = [(a[i], b[i]) for i in indices]

    # Step 1: Merge intervals
    merged = []
    for start, end in intervals:
        if not merged or merged[-1][1] < start:  # FIXED CONDITION
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)

    # Step 2: Find gaps between merged intervals
    gaps = []
    for i in range(1, len(merged)):
        prev_end = merged[i - 1][1]
        curr_start = merged[i][0]
        gap = curr_start - prev_end - 1
        if gap >= 0:
            gaps.append(gap)

    # Step 3: Sort gaps and try to bridge them with interval of length ≤ k
    gaps.sort()
    components = len(merged)

    for gap in gaps:
        if gap <= k:
            components -= 1
            break  # Only one interval can be added

    return components
