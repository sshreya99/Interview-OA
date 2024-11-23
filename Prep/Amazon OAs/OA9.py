# maximize the similarity between inv1 and inv2 (inventory optimizer)
# https://leetcode.com/discuss/interview-question/5975642/
# TC: O(N) SC: 0(N)

def maximize_similarity(n, inv1, inv2):
    """
    Maximizes the similarity between two inventories by redistributing values within inv1.
    
    Args:
        n (int): Number of elements in each inventory.
        inv1 (list[int]): First inventory.
        inv2 (list[int]): Second inventory.
    
    Returns:
        int: Maximum similarity between inv1 and inv2.
    """
    # Count the initial similarity
    similarity = 0
    unmatched = []

    for i in range(n):
        if inv1[i] == inv2[i]:
            similarity += 1
        else:
            # Store unmatched indices and the difference
            unmatched.append((i, inv2[i] - inv1[i]))

    # Check if we can redistribute using the unmatched differences
    pos_sum = 0  # Positive surplus in unmatched indices
    neg_sum = 0  # Negative deficit in unmatched indices

    for _, diff in unmatched:
        if diff > 0:
            pos_sum += diff
        else:
            neg_sum += diff

    # The minimum of positive and absolute negative surplus determines how much we can fix
    similarity += min(pos_sum, -neg_sum)

    return similarity


# Example Usage
n = 3
inv1 = [2, 4, 1]
inv2 = [1, 2, 3]
result = maximize_similarity(n, inv1, inv2)
print(result)  # Output: 2
