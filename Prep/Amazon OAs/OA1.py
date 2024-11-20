#https://leetcode.com/discuss/interview-question/6044882/amazon-online-assessment-question-2024-november/2722584

def min_total_effort(effort):
    # Sort the array
    effort.sort()
    # Use a regular dictionary to store the minimum effort for each divisor
    min_effort = {}
    
    # Initialize the total sum
    total_effort = 0
    
    # Process each effort in sorted order
    for e in effort:
        # Start with the current effort as the minimum value
        smallest_effort = e
        
        # Find divisors of the current value
        for i in range(1, int(e**0.5) + 1): # the biggest divisor can be that value itself. so, from 1 to square root of that value e range. 
            if e % i == 0:
                # Check both divisors (i and e // i) if they exist in the map
                if i in min_effort:
                    smallest_effort = min(smallest_effort, min_effort[i])
                if (e // i) in min_effort:
                    smallest_effort = min(smallest_effort, min_effort[e // i])
        
        # Update the map for the current number
        min_effort[e] = smallest_effort
        
        # Add the smallest effort to the total
        total_effort += smallest_effort
    
    return total_effort

# Example usage
effort = [3, 6, 2, 5, 25]
print(min_total_effort(effort))  # Output: 17
