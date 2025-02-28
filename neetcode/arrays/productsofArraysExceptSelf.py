class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        sizes, ansStr = [], ""
        for str1 in strs:
            sizes.append(len(str1))
        for sz in sizes:
            ansStr += str(sz)
            ansStr += ","
        ansStr += "#"
        for str1 in strs:
            ansStr += str1
        print(ansStr)
        return ansStr
    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        sizes, res, i = [], [], 0
        while s[i]!="#":
            cur = ""
            while s[i] != ",":
                cur += s[i]
                i += 1
            sizes.append(int(cur))
            i+=1
        # print(sizes)
        i+=1
        for sz in sizes:
            res.append(s[i:i + sz])
            i += sz
        return res
