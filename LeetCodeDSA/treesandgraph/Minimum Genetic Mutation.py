class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:


        poss = ['A', 'C', 'G', 'T']
        valid = set(bank)
        valid.add(startGene)

        q = deque([(startGene, 0)])
        if endGene not in valid:
            return -1

        seen = set()

        while q:
            curr_gene, curr_steps = q.popleft()
            if curr_gene == endGene:
                return curr_steps

            for i in range(8):
                for ch in poss:
                    if ch == curr_gene[i]:
                        continue
                    poss_val = curr_gene[:i] + ch + curr_gene[i+1:]
                    if poss_val not in seen and poss_val in valid:
                        q.append((poss_val, curr_steps + 1))
                        seen.add(poss_val)

        return -1











