# https://leetcode.com/discuss/interview-question/5328967/Amazon-OA-or-SDE-1-or-Results-Awaited

# 1: Password strength

# Input String: hackerrank
# Expected output: 3

# Explaination: hack er rank
# Solution:
# Simply iterated and calculated vowels and consonants in variables. In case both variables were greater than 1, inreased cnt by 1 and reset the vowel and consonant count to 0.
# This was a simple O(n) solution with all test cases passed.

def FindPasswordStrength(string):
    vCount = 0
    cCount = 0
    total_count = 0
    vowels = "aeiou"
    for i in string:
        if i in vowels:
            vCount = vCount+1
        else:
            cCount = cCount+1
        if vCount > 0 and cCount > 0:
            vCount = 0
            cCount = 0
            total_count = total_count+1
    return total_count


print(FindPasswordStrength("hackerrank"))    

# find steps:
# TC:O(n*m) SC: O(n*m)
def shortest_steps_to_destination(grid):
    rows, cols = len(grid), len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, down, left, right
    queue = [(0, 0, 0)]  # Start from top-left corner with 0 steps
    # To track visited cells

    while queue:
        # Simulate queue using list pop(0)
        x, y, steps = queue.pop(0)

        # If we reach the destination (cell with 9)
        if grid[x][y] == 9:
            return steps

        # Mark the cell as visited
        
        grid[x][y] = 2
        # Explore all possible directions
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            # Check bounds, obstacles, and if the cell is already visited
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] != 1 and grid[nx][ny] != 2:
                queue.append((nx, ny, steps + 1))  # Add the new cell to the queue
              
    return -1  # Return -1 if there's no path to the destination

# Example usage
grid = [
    [0, 1, 0],
    [0, 0, 0],
    [1, 9, 1]
]
print(shortest_steps_to_destination(grid))  # Output: 3

