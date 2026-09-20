class Solution:
    def reverseDegree(self, s: str) -> int:

        ch, idx = 0, 1
        res = 0
        for ch in s:
            res += (123 - ord(ch))*idx
            idx += 1
        return res


        # map_ = {
        #     'a':26,
        #     'b':25,
        #     'c':24,
        #     'd':23,
        #     'e':22,
        #     'f':21,
        #     'g':20,
        #     'h':19,
        #     'i':18,
        #     'j':17,
        #     'k':16,
        #     'l':15,
        #     'm':14,
        #     'n':13,
        #     'o':12,
        #     'p':11,
        #     'q':10,
        #     'r':9,
        #     's':8,
        #     't':7,
        #     'u':6,
        #     'v':5,
        #     'w':4,
        #     'x':3,
        #     'y':2,
        #     'z':1
        # }
        # res = 0
        # for idx, ch in enumerate(s):
        #     res += (map_[ch]*(idx+1))

        # return res 
        