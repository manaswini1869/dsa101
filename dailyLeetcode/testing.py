# Exercise block. Do not change the function input parameters.


def is_palindrome_fixed(sentence):
    # Your code here
    cleaned = "".join(char.lower() for char in sentence if char.isalnum())

    left, right = 0, len(cleaned) - 1
    while left <= right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    return True


def is_palindrome(sentence):
    # Compare characters from both ends
    left, right = 0, len(sentence)-1
    while left <= right:
        if sentence[left] != sentence[right]:
            return False
        left += 1
        right -= 1
    return True