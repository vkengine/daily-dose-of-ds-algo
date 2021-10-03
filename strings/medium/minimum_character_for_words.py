"""
Write a function that takes in an array of words and returns the smallest array of characters needed to form all of the words. The characters don't need to be in any particular order.

For example, the characters ["y", "r", "o", "u"] are needed to form the words ["your", "you", "or", "yo"].

Note: the input words won't contain any spaces; however, they might contain punctuation and/or special characters.

Sample Input
words = ["this", "that", "did", "deed", "them!", "a"]
Sample Output
["t", "t", "h", "i", "s", "a", "d", "d", "e", "e", "m", "!"]
// The characters could be ordered differently.
"""


# O(n * l) time | O(c) space - where n is the number of words,
# l is the length of the longest word, and c is the number of unique
# characters across all words See notes under video explanation for details about the space complexity.
def minimumCharactersForWords(words):
    # Write your code here.
    final_char_with_frequecy = {}
    minimum_characters = []

    for word in words:
        frequecy = {}
        for char in word:
            if char not in frequecy:
                frequecy[char] = 1
            else:
                frequecy[char] += 1
        for key, value in frequecy.items():
            if key not in final_char_with_frequecy:
                final_char_with_frequecy[key] = value
            else:
                if final_char_with_frequecy[key] > value:
                    continue
                else:
                    final_char_with_frequecy[key] = value

    for key, value in final_char_with_frequecy.items():
        for i in range(value):
            minimum_characters.append(key)

    return minimum_characters
