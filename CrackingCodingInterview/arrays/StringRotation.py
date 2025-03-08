def isSubstring(s1: str, s2: str) -> bool:
    return s2 in s1

def StringRotation(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False

    s1_s2 = s1 + s1
    print()
    return isSubstring(s1_s2, s2)


def test_StringRotation():
    # Test case 1: Normal rotation
    s1 = "waterbottle"
    s2 = "erbottlewat"
    assert StringRotation(s1, s2) == True, f"Test case 1 failed"

    # Test case 2: Same strings, no rotation
    s1 = "hello"
    s2 = "hello"
    assert StringRotation(s1, s2) == True, f"Test case 2 failed"

    # Test case 3: Different length strings (cannot be rotation)
    s1 = "abc"
    s2 = "abcd"
    assert StringRotation(s1, s2) == False, f"Test case 3 failed"

    # Test case 4: Rotation with different characters
    s1 = "abcdef"
    s2 = "defabc"
    assert StringRotation(s1, s2) == True, f"Test case 4 failed"

    # Test case 5: Edge case - Empty strings
    s1 = ""
    s2 = ""
    assert StringRotation(s1, s2) == True, f"Test case 5 failed"

    # Test case 6: Edge case - One empty string, one non-empty string
    s1 = "hello"
    s2 = ""
    assert StringRotation(s1, s2) == False, f"Test case 6 failed"

    # Test case 7: Larger string with rotation
    s1 = "1234567890"
    s2 = "7890123456"
    assert StringRotation(s1, s2) == True, f"Test case 7 failed"

    # Test case 8: Strings with different characters (not a rotation)
    s1 = "abcdefg"
    s2 = "xyzabcdef"
    assert StringRotation(s1, s2) == False, f"Test case 8 failed"

    # Test case 9: Strings that contain all characters in different orders
    s1 = "xyzabc"
    s2 = "zabcxy"
    assert StringRotation(s1, s2) == True, f"Test case 9 failed"

    # Test case 10: Long strings with a valid rotation
    s1 = "a" * 10000 + "b" * 10000
    s2 = "b" * 10000 + "a" * 10000
    assert StringRotation(s1, s2) == True, f"Test case 10 failed"

    print("All test cases passed!")

# Run the test cases
test_StringRotation()
