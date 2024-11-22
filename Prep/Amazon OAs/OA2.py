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

def findSteps(arr):
    sr = 0
    sc = 0
    dir = [(-1, 0), (1, 0), (0, -1), (0, 1)] # U D L R
    


arr = [[0, 1, 0], [0, 0, 0], [1, 9, 1]]   
print(findSteps(arr))
