def isUnique(s: str) -> bool:
    s_char = []
    for char in s:
        if char in s_char:
            return False
        s_char.append(char)
    return True

test_strings = [
    "abcdefg",          # Unique characters
    "hello",            # Not unique (duplicate 'l')
    "a",               # Single character, unique
    "",                # Empty string, unique by default
    "abcdefghijklmnopqrstuvwxyz",  # All unique
    "abc123!@#",       # Unique with special characters
    "112233",          # Not unique (repeating digits)
    "AbCDefG",         # Unique (case-sensitive)
    "aAbBcC",          # Not unique (repeating case variations)
    "abcdefghijklmnopqrstuvwxyza", # Not unique (duplicate 'a')
    "hello world"      # Not unique (space and repeating letters)
]

for test_str in test_strings:
    print(isUnique(test_str))