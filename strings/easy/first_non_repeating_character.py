"""
Write a function that takes in a string of lowercase English-alphabet letters and returns the index of the string's
first non-repeating character.
The first non-repeating character is the first character in a string that occurs only once.
If the input string doesn't have any non-repeating characters, your function should return -1.
Sample Input
string = "abcdcaf"
Sample Output
1 // The first non-repeating character is "b" and is found at index 1
"""


# O(n) time | O(1) space
# O(1) space how ??
def firstNonRepeatingCharacter(string):
    # Write your code here.
    index = -1

    char_count = {}

    for char in string:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1

    for key, value in char_count.items():
        if value == 1:
            index = string.index(key)
            break

    return index
