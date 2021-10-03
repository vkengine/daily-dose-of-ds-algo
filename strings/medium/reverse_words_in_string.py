"""
Write a function that takes in a string of words separated by one or more whitespaces and returns a string that
has these words in reverse order. For example, given the string "tim is great",
your function should return "great is tim".

For this problem, a word can contain special characters, punctuation, and numbers.
The words in the string will be separated by one or more whitespaces, and the reversed string must contain the same
whitespaces as the original string. For example, given the string "whitespaces    4"
you would be expected to return "4    whitespaces".

Note that you're not allowed to to use any built-in split or reverse methods/functions.
However, you are allowed to use a built-in join method/function.

Also note that the input string isn't guaranteed to always contain words.

Sample Input
string = "I am the best!"
Sample Output
"best! the am I"
"""


# O(n) time | O(n) space
def reverseWordsInString(string):
    # Write your code here.
    string_as_list = string.split(" ")
    final_string = []

    len_to_interate = len(string_as_list)

    for i in range(len_to_interate):
        final_string.append(string_as_list.pop())

    return " ".join(final_string)


# O(n) time | O(n) space
def reverseWordsInString_part_2(string):
    words = []
    startOfWord = 0
    for idx in range(len(string)):
        character = string[idx]
        if character == " ":
            words.append(string[startOfWord:idx])
            startOfWord = idx
        elif string[startOfWord] == " ":
            words.append(" ")
            startOfWord = idx
    words.append(string[startOfWord:])
    reverseList(words)
    return "".join(words)


def reverseList(list):
    start, end = 0, len(list) - 1
    while start < end:
        list[start], list[end] = list[end], list[start]
        start += 1
        end -= 1
