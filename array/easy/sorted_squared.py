"""
Sorted Squared Array
Write a function that takes in a non-empty array of integers that are sorted in ascending order and
returns a new array of the same length with the squares of the original integers also sorted in ascending order.

Sample Input
array = [1, 2, 3, 5, 6, 8, 9]
Sample Output
[1, 4, 9, 25, 36, 64, 81]
"""

def sortedSquaredArray(array):
    # Write your code here.

    pointer_min_element = 0
    pointer_max_element = len(array) - 1

    return_array = [0 for _ in array]

    for idx in reversed(range(len(array))):
        small_value = array[pointer_min_element]
        large_value = array[pointer_max_element]

        if abs(small_value) > abs(large_value):
            return_array[idx] = small_value * small_value
            pointer_min_element += 1
        else:
            return_array[idx] = large_value * large_value
            pointer_max_element -= 1

    return return_array