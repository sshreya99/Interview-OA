# https://leetcode.com/discuss/interview-question/5988967/amazon-sde-i-india-online-assessment/

# the story of amazon - novel

# TC:O(n) SC:O(n)
# USE DIFF VARIABLES
def buyVolumes(daily_volumes: list[int]) -> list[list[int]]:
    """
    Determines which volumes can be purchased each day based on availability and prerequisites.
    
    Args:
        daily_volumes: List where daily_volumes[i] represents the volume number that becomes
                      available on day i.
    
    Returns:
        List of lists where result[i] contains either:
        - The volume numbers purchased on day i in ascending order
        - [-1] if no volumes could be purchased on day i
    """
    total_volumes = len(daily_volumes)
    
    # Track which volumes are available for purchase
    volume_available = [False for _ in range(total_volumes)]
    
    # Store the volumes purchased each day
    daily_purchases = [list() for _ in range(total_volumes)]
    
    # Keep track of the next volume we need for sequential reading
    next_required_volume = 0
    
    for current_day, new_volume in enumerate(daily_volumes):
        # Mark the new volume as available
        volume_available[new_volume - 1] = True
        
        # Purchase all available sequential volumes
        while (next_required_volume < total_volumes and 
               volume_available[next_required_volume]):
            daily_purchases[current_day].append(next_required_volume + 1)
            next_required_volume += 1
            
        # If no purchases were made today, append -1
        if len(daily_purchases[current_day]) == 0:
            daily_purchases[current_day].append(-1)
            
    return daily_purchases
    
print(buyVolumes([2, 1, 4, 3]))
print(buyVolumes([1, 4, 3, 2, 5]))
print(buyVolumes([1, 2, 3]))

# all packages with equal cost
# TC: O(n + k^2 ) where k is total number of unique costs. in all unique value case O(n^2) SC: O(n)
# USE DIFF VARIABLES
from collections import defaultdict

def findMaximumPackages(cost: list[int]) -> int:
    """
    Finds the maximum number of packages that can be created with equal total costs.
    Each package can contain at most 2 items.
    
    Args:
        cost: List of individual item costs
        
    Returns:
        Maximum number of packages possible where all packages have equal total cost
    
    Example:
        >>> findMaximumPackages([2, 1, 3])
        2  # Can make two packages: [3] and [1, 2], both with total cost 3
    """
    # Count frequency of each cost
    cost_frequency = defaultdict(int)
    for single_cost in cost:
        cost_frequency[single_cost] += 1
    
    # Get unique costs
    unique_costs = list(cost_frequency.keys())
    num_unique_costs = len(unique_costs)
    
    # Track frequency of each possible package total cost
    package_cost_frequency = defaultdict(int)
    
    # Process each unique cost
    for i in range(num_unique_costs):
        current_cost = unique_costs[i]
        
        # Single item packages
        package_cost_frequency[current_cost] += cost_frequency[current_cost]
        
        # Two identical items packages
        package_cost_frequency[2 * current_cost] += (cost_frequency[current_cost] // 2)
        
        # Two different items packages
        for j in range(i + 1, num_unique_costs):
            other_cost = unique_costs[j]
            combined_cost = current_cost + other_cost
            possible_pairs = min(cost_frequency[current_cost], 
                               cost_frequency[other_cost])
            package_cost_frequency[combined_cost] += possible_pairs
    
    # Return the maximum number of packages possible with equal cost
    return max(package_cost_frequency.values())
    
print(findMaximumPackages([2, 1, 3]))  # Expected: 2
print(findMaximumPackages([4, 5, 10, 3, 1, 2, 2, 2, 3]))  # Expected: 4
print(findMaximumPackages([1, 1, 2, 2, 1, 4]))  # Expected: 3
print(findMaximumPackages([10, 2, 1]))  # Expected: 1
