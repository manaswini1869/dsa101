class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        numsSorted = sorted(nums)
        currGroup = 0
        numToGroup = {}
        numToGroup[numsSorted[0]] = currGroup

        groupToList = {}
        groupToList[currGroup] = deque([numsSorted[0]])

        for i in range(1, len(nums)):
            if (abs(numsSorted[i] - numsSorted[i-1])) > limit:
                currGroup += 1

            numToGroup[numsSorted[i]] = currGroup

            if currGroup not in groupToList:
                groupToList[currGroup] = deque()
            groupToList[currGroup].append(numsSorted[i])
        for i in range(len(nums)):
            num = nums[i]
            group = numToGroup[num]
            nums[i] = groupToList[group].popleft()
        return nums