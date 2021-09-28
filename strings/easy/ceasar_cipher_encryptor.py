"""
Given a non-empty string of lowercase letters and a non-negative integer representing a key,
write a function that returns a new string obtained by shifting every letter in the input string by k positions in the
alphabet.
where k is the key.
Note that letters should "wrap" around the alphabet; in other words, the letter z shifted by one returns the letter a.

Sample Input :
string = "xyz"
key = 2
Sample Output = "zab"
"""


# O(n) time | O(n) space
def caesarCipherEncryptor(string, key):
    characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
                  'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                  'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
                  'x', 'y', 'z']

    final_string = []

    for char in string:
        current_index = characters.index(char)
        final_string.append(characters[(current_index + key) % 26])

    return "".join(final_string)
