from collections import Counter

def PalindromePermutation(s: str) -> bool:
    s = s.replace(" ", "").lower()
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    odd_count = sum(1 for count in char_count.values() if count % 2 == 1)
    return odd_count <= 1

test_strings = [
    "taco cat",      # True, a palindrome permutation
    "aabb",          # True, a palindrome permutation
    "abc",           # False, not a palindrome permutation
    "racecar",       # True, a palindrome permutation
    "hello",         # False, not a palindrome permutation
    "A man a plan a canal Panama",  # True, palindrome permutation
    "abccba",        # True, a palindrome permutation
    "random string", # False, not a palindrome permutation
    "Aba",           # True, a palindrome permutation
    "racedar",       # True, a palindrome permutation
]

for string in test_strings:
    print(PalindromePermutation(string))