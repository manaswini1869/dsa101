class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        weights = {}

        def union(dividend, divisor, quotient):
            dividend_grid, dividend_weight = find(dividend)
            divisor_grid, divisor_weight = find(divisor)
            if dividend_grid != divisor_grid:
                weights[dividend_grid] = (divisor_grid, divisor_weight * quotient / dividend_weight)


        def find(node_id):
            if node_id not in weights:
                weights[node_id] = (node_id, 1)
            group_id, weight = weights[node_id]
            if group_id != node_id:
                new_group_id, new_weight = find(group_id)
                weights[node_id] = (new_group_id, weight*new_weight)
            return weights[node_id]

        for (dividend, divisor), quotient in zip(equations, values):
            union(dividend, divisor, quotient)

        results = []
        print(weights)
        for (dividend, divisor) in queries:
            if dividend not in weights or divisor not in weights:
                results.append(-1.0)
            else:
                dividend_grid, dividend_weight = find(dividend)
                divisor_grid, divisor_weight = find(divisor)
                if dividend_grid != divisor_grid:
                    results.append(-1.0)
                else:
                    results.append(dividend_weight / divisor_weight)
        return results