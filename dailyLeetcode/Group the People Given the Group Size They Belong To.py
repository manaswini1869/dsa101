from collections import defaultdict
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = []
        hash_groups = defaultdict(list)
        for idx, val in enumerate(groupSizes):
            hash_groups[val].append(idx)
        for size, people in hash_groups.items():
            for i in range(0, len(people), size):
                groups.append(people[i:i+size])
        print(groups)
        return groups