class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        minimum_count = 0
        hash_answers = {}
        for answer in answers:
            hash_answers[answer] = hash_answers.get(answer, 0) + 1
        for x, cnt in hash_answers.items():
            group_size = x + 1
            num_groups = ceil(cnt / group_size)
            minimum_count += num_groups * group_size
        return minimum_count
