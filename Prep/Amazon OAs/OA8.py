#performance
#not sure
int getMaximumPartitions(const vector<int>& performance) {
    int ans = 0, x = -1;
    for (const auto v : performance)
        (x &= v) || (ans -= --x);
    return max(ans, 1);
}
 
# probably this works
# TC: O(n) SC: O(1)
def maximize_partitions(performance):
    """
    Finds the maximum number of partitions such that the total bottleneck level
    (bitwise AND of each partition) is minimized.

    Args:
        performance (list[int]): The performance levels of the components.

    Returns:
        int: The maximum number of partitions.
    """
    n = len(performance)
    if n == 0:
        return 0

    current_bottleneck = performance[0]
    partitions = 0

    for i in range(n):
        # Perform bitwise AND for the current partition
        current_bottleneck &= performance[i]

        # If the bottleneck becomes 0, create a new partition
        if current_bottleneck == 0:
            partitions += 1
            # Reset the bottleneck to the next element if any
            if i < n - 1:
                current_bottleneck = performance[i + 1]
            else:
                break  # No more elements to process

    # If there are elements left after the last partition, count one more partition
    if current_bottleneck != 0:
        partitions += 1

    return partitions


# Example Usage
performance = [5, 2, 6, 1, 1, 4]
result = maximize_partitions(performance)
print(result)  # Output: 3
