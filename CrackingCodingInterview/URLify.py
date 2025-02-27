def URLify(s: str) -> str:
    list_s = list(s)
    for i in range(len(s)):
        if list_s[i] == " ":
            list_s[i] = "%20"
    return "".join(list_s)

test_cases = [
    ("Mr John Smith", "Mr%20John%20Smith"),  # Expected: "Mr%20John%20Smith"
    ("Hello World", "Hello%20World"),        # Expected: "Hello%20World"
    ("NoSpaces", "NoSpaces"),                # Expected: "NoSpaces" (No change)
    (" leading", "%20leading"),              # Expected: "%20leading"
    ("trailing ", "trailing%20"),            # Expected: "trailing%20"
    ("  multiple  spaces  ", "%20%20multiple%20%20spaces%20%20"),
    # Expected: "%20%20multiple%20%20spaces%20%20"
    ("", ""),                                # Expected: "" (Empty string)
    (" ", "%20"),                            # Expected: "%20" (Single space)
]

for strings in test_cases:
    print(URLify(strings[0]) == strings[1])