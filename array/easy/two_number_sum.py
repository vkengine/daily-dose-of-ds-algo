"""Two Number Sum Write a function that takes in a non-empty array of distinct integers and an integer representing a
target sum. If any two numbers in the input array sum up to the target sum, the function should return them in an
array, in any order. If no two numbers sum up to the target sum, the function should return an empty array.

Note that the target sum has to be obtained by summing two different integers in the array;
you can't add a single integer to itself in order to obtain the target sum.

assume that there will be at most one pair of numbers summing up to the target sum.
"""


# O(n) time | O(n) space
def solution_one(array, targetSum):
    hash_table = {}
    for num in array:
        value = targetSum - num
        if value in hash_table:
            return [value, num]
        else:
            hash_table[num] = True
        return []


# O(nlog(n)) time | O(1) space
def solution_two(array, targetSum):
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            return [array[left], array[right]]
        elif currentSum < targetSum:
            left += 1
        elif currentSum > targetSum:
            right -= 1
    return []