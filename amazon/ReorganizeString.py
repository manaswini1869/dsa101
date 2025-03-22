from collections import Counter
class Solution:
    def reorganizeString(self, s: str) -> str:
        ans = []
        pq = [(-freq, char) for char, freq in Counter(s).items()] # creating a max heap from the string character and frequency
        heapify(pq)
        while pq:
            count_first, char_first = heappop(pq)
            if not ans or char_first != ans[-1]:
                ans.append(char_first)
                if count_first + 1 != 0:
                    heappush(pq, (count_first+1, char_first))
            else:
                if not pq:
                    return ""
                count_second, char_second = heappop(pq) # choosing a different character as last element in ans is same as the popped element
                ans.append(char_second)
                if count_second + 1 != 0:
                    heappush(pq, (count_second+1, char_second))
                heappush(pq, (count_first, char_first)) # pushing the original popped elements back in the priority queue

        return "".join(ans)