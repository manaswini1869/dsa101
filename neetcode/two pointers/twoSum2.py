class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pervMap = defaultdict(int)
        for i in range(len(numbers)):
            temp = target - numbers[i]
            if pervMap[temp]:
                return [pervMap[temp], i+1]
            pervMap[numbers[i]] = i+1
        return []