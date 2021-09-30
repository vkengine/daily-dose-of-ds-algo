"""
Group Anagrams
Write a function that takes in an array of strings and groups anagrams together.
Anagrams are strings made up of exactly the same letters, where order doesn't matter. For example,
"cinema" and "iceman" are anagrams; similarly, "foo" and "ofo" are anagrams.
Your function should return a list of anagram groups in no particular order.
Sample Input
words = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
Sample Output
[["yo", "oy"], ["flop", "olfp"], ["act", "tac", "cat"], ["foo"]]
"""


# O(w * n * log(n)) time | O(wn) space - where w is the number of words and
# n is the length of the longest word
def groupAnagrams(words):
    # Write your code here.
    group_together = {}

    for i in words:
        sorted_word = "".join(sorted(i))
        if sorted_word not in group_together:
            group_together[sorted_word] = [i]
        else:
            group_together[sorted_word].append(i)

    return list(group_together.values())
