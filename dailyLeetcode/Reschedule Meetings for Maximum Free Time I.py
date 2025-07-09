class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        freespace = [startTime[0]]

        for i in range(1, len(startTime)):
            freespace.append(startTime[i] - endTime[i-1])

        if endTime[-1] != eventTime:
            freespace.append(eventTime - endTime[-1])

        pre = [0]
        n = len(freespace)
        for i in range(n):
            pre.append(pre[-1] + freespace[i])

        maxi = 0
        n = len(pre)
        for i in range(k, n):
            maxi = max(maxi, pre[i] - pre[max(i - k - 1, 0)])

        return max(maxi, max(freespace))