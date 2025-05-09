# kind of palindrome but twist

def count_special_substrings(genome: str) -> int:
    n = len(genome)
    count = 0

    # Type 1: Length-2 substrings with equal characters
    for i in range(n - 1):
        if genome[i] == genome[i + 1]:
            count += 1

    # Type 2: Length >= 3, first and last equal, middle has exactly one unique character
    for i in range(n):
        for j in range(i + 2, n):
            if genome[i] == genome[j]:
                middle = genome[i+1:j]
                if len(set(middle)) == 1:
                    count += 1

    return count
