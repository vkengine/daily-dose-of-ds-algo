# O(n) time | O(1) space
def isPalindrome(string):
    # Write your code here.
    left_idx = 0
    right_idx = len(string) - 1

    while left_idx < right_idx:
        if string[left_idx] != string[right_idx]:
            return False
        left_idx += 1
        right_idx -= 1
    return True


# O(n) time | O(n) space
def isPalindrome_2(string):
    # Write your code here.
    return string[::-1] == string
