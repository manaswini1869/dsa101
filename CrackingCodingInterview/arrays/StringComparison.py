def StringCompression(s: str) -> str:
    if not s:
        return s
    res = ""
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            res += s[i-1] + str(count)
            count = 1
    res += s[-1] + str(count)
    if len(res) > len(s):
        return s
    else:
        return res

print(StringCompression("aaabbbbbcaa"))

