class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        cannot_comm = set()

        for u, v in friendships:
            can_comm = False
            u_languages = set(languages[u-1])
            for language in languages[v-1]:
                if language in u_languages:
                    can_comm = True
                    break

            if not can_comm:
                cannot_comm.add(u)
                cannot_comm.add(v)
        if not cannot_comm:
            return 0

        count = [0] * n
        for people in cannot_comm:
            for language in languages[people-1]:
                count[language - 1] += 1

        max_count = 0
        for cn in count:
            max_count = max(max_count, cn)

        return len(cannot_comm) - max_count

