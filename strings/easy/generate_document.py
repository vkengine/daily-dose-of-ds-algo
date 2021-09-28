"""You're given a string of available characters and a string representing a document that you need to generate.
Write a function that determines if you can generate the document using the available characters. If you can generate
the document, your function should return true; otherwise, it should return false.

You're only able to generate the document if the frequency of unique characters in the characters string is greater
than or equal to the frequency of unique characters in the document string. For example, if you're given characters =
"abcabc" and document = "aabbccc" you cannot generate the document because you're missing one c.

The document that you need to create may contain any characters, including special characters, capital letters,
numbers, and spaces.

Note: you can always generate the empty string ("").
"""


# O(m * (n + m)) time | O(1) space
# HORRIBLE SOLUTION
def generateDocument(characters, document):
    # Write your code here.

    current_result = True
    for char in document:
        if char in characters:
            characters = characters.replace(char, "", 1)
        else:
            current_result = False
        print(characters)

    return current_result


# O(n + m) time | O(1) space
# GOOD solution
def generate_document(characters, document):
    # Write your code here.
    key_count = {}

    for char in characters:
        if char not in key_count:
            key_count[char] = 1
        else:
            key_count[char] += 1

    for char in document:
        if char in key_count:
            if key_count[char] > 0:
                key_count[char] -= 1
            else:
                return False
        else:
            return False

    return True
