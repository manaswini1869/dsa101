def checkPermutations(str1: str, str2:str) -> bool:
    # testing str2 a permutation of str1
    if (len(str2) != len(str1)):
        return False
    str1_hash, str2_hash = {}, {}
    for i in range(len(str1)):
        str1_hash[str1[i]] = str1_hash.get(str1[i], 0) + 1
        str2_hash[str2[i]] = str2_hash.get(str2[i], 0) + 1
    return str1_hash == str2_hash

test_cases = [
    ("abc", "bca"),         # Permutation (Expected: True)
    ("hello", "olelh"),     # Permutation (Expected: True)
    ("test", "ttew"),       # Not a permutation (Expected: False)
    ("abcd", "abcde"),      # Different lengths (Expected: False)
    ("", ""),               # Both empty (Expected: True)
    ("aabbcc", "abcabc"),   # Permutation (Expected: True)
    ("12345", "54321"),     # Permutation (Expected: True)
    ("apple", "pale"),      # Not a permutation (Expected: False)
    ("same", "same"),       # Same string (Expected: True)
    ("AaBb", "bBaA"),       # Permutation (Expected: True, if case-sensitive)
    ("abcd", "abce"),       # One different character (Expected: False)
]

for strings in test_cases:
    print(checkPermutations(strings[0], strings[1]))