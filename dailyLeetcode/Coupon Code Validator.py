class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:

        n = len(code)
        res = {'electronics':[], 'grocery':[], 'pharmacy':[], 'restaurant':[]}
        pattern = r'^[a-zA-Z0-9_]+$'
        business = set(['electronics', 'grocery', 'pharmacy', 'restaurant'])
        for i in range(n):
            c = code[i]
            b = businessLine[i]
            a = isActive[i]

            if re.fullmatch(pattern, c) and b in business and a:
                res[b].append(c)
        result = []
        if res['electronics']:
            result += sorted(res['electronics'])
        if res['grocery']:
            result += sorted(res['grocery'])
        if res['pharmacy']:
            result += sorted(res['pharmacy'])
        if res['restaurant']:
            result += sorted(res['restaurant'])
        return result




import re
from typing import List

class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        res = {
            'electronics': [],
            'grocery': [],
            'pharmacy': [],
            'restaurant': []
        }

        pattern = r'^[a-zA-Z0-9_]+$'

        for c, b, a in zip(code, businessLine, isActive):
            if a and b in res and re.fullmatch(pattern, c):
                res[b].append(c)

        result = []
        for category in ['electronics', 'grocery', 'pharmacy', 'restaurant']:
            result.extend(sorted(res[category]))

        return result
