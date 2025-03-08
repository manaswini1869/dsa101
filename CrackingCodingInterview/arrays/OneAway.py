def OneAway(s1: str, s2:str) -> bool:
    hash_s1 = {}
    hash_s2 = {}
    for char in s1:
        hash_s1[char] = hash_s1.get(char, 0) + 1
    for char in s2:
        hash_s2[char] = hash_s2.get(char, 0) + 1
    differences = 0
    for k in set(hash_s1.keys()).union(hash_s2.keys()):
        count_diff = abs(hash_s1.get(k,0) - hash_s2.get(k,0))
        if count_diff > 1:
            return False
    return True

test_cases = [
    # Test Case 1: Same string (no edits)
    ("pale", "pale", True),

    # Test Case 2: One replacement
    ("pale", "bale", True),

    # Test Case 3: One insertion
    ("pale", "pales", True),

    # Test Case 4: One removal
    ("pales", "pale", True),

    # Test Case 5: More than one edit (requires two replacements)
    ("pale", "bake", False),

    # Test Case 6: More than one edit (requires two replacements)
    ("pale", "bake", False),

    # Test Case 7: Empty string and non-empty string (one insertion)
    ("", "a", True),

    # Test Case 8: Same length, multiple differences
    ("pale", "bake", False),

    # Test Case 9: Single character insertion
    ("abc", "abac", True),

    # Test Case 10: One character change
    ("cat", "bat", True),

    # Test Case 11: One removal, different positions
    ("dog", "do", True),

    # Test Case 12: Non-matching length, too many differences
    ("apple", "applesauce", False)
]
for string in test_cases:
    print(OneAway(string[0], string[1]) == string[2])