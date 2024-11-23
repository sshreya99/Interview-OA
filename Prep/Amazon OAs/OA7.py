# Product identifiers, operation analyst string
# NOT SURE
# TC:O(N) SC: O(1)

def maximize_score(initial_str):
    """
    Finds the maximum number of operations that can be performed on the string
    while ensuring its type remains the same as the initial string's type.

    Args:
        initial_str (str): The initial product identifier string.

    Returns:
        int: The maximum number of valid operations.
    """
    if len(initial_str) == 0:
        return 0
    
    res = 0
    start_char = initial_str[0]
    end_char = initial_str[-1]
    s = 0

    for i, c in enumerate(initial_str):
        if c == start_char:
            s = i
        elif c == end_char:
            res = max(res, s + len(initial_str) - 1 - i)
        
        if start_char == end_char:
            res = max(res, i + len(initial_str) - 1 - i)
    
    return res


# Example Usage
str1 = "aabab"
print(maximize_score(str1))  # Output: 3

str2 = "hchc"
print(maximize_score(str2))  # Output: 2

str3 = "abbc"
print(maximize_score(str3))  # Output: 0
