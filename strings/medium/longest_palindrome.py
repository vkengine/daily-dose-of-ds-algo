"""
Write a function that, given a string, returns its longest palindromic substring.
A palindrome is defined as a string that's written the same forward and backward.
Note that single-character strings are palindromes.
You can assume that there will only be one longest palindromic substring.

Sample Input
string = "abaxyzzyxf"
Sample Output
"xyzzyx"
"""


# O(n^2) time | O(n) space
def longestPalindromicSubstring(string):
    # Write your code here.
    current_longest = [0, 1]
    for i in range(1, len(string)):
        odd = get_longest_palindrome(string, i - 1, i + 1)
        even = get_longest_palindrome(string, i - 1, i)
        longest = max(odd, even, key=lambda x: x[1] - x[0])
        current_longest = max(longest, current_longest, key=lambda x: x[1] - x[0])

    return string[current_longest[0]: current_longest[1]]


def get_longest_palindrome(string, left_idx, right_idx):
    while left_idx >= 0 and right_idx < len(string):
        if string[left_idx] != string[right_idx]:
            break
        left_idx -= 1
        right_idx += 1

    return [left_idx + 1, right_idx]
