class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:

        n = len(prices)
        answer = prices.copy()
        stack = []
        for i in range(n):
            while stack and prices[stack[-1]] >= prices[i]:
                answer[stack.pop()] -= prices[i]

            stack.append(i)

        # for i in range(n):
        #     answer.append(prices[i])
        #     for j in range(i+1, n):
        #         if prices[j] <= answer[-1]:
        #             answer[-1] = answer[-1] - prices[j]
        #             break

        return answer