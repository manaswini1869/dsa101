class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        str_n = str(n)
        hash_counter = {}
        for i in str_n:
            hash_counter[i] = hash_counter.get(i, 0) + 1

        def combinations(combo, counter):
            if len(combo) == len(str_n):
                if combo[0] == '0':
                    return False
                int_combo = int(combo)
                return int_combo > 0 and (int_combo & (int_combo - 1)) == 0

            for i in counter:
                if counter[i] > 0:
                    counter[i] -= 1

                    if combinations(combo + i, counter):
                        return True
                    counter[i] += 1
                
            return False

        return combinations('', dict(hash_counter))