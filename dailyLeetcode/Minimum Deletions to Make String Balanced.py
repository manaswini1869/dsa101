class Solution:
    def minimumDeletions(self, s: str) -> int:

        n = len(s)
        a_count = 0
        for i in range(n):
            if s[i] == 'a':
                a_count += 1
        
        b_count = 0
        count = n

        for ch in s:
            if ch == 'a':
                a_count -= 1
            count = min(count, a_count+b_count)
            if ch == 'b':
                b_count += 1
        return count

        # time complexity = O(n)
        # space complexity = O(1)
            


        return count

        # n = len(s)
        # count_a = [0]*n
        # a_count = 0

        # for i in range(n-1, -1, -1):
        #     count_a[i] = a_count
        #     if s[i] == 'a':
        #         a_count += 1
        
        # count = n
        # b_count = 0
        # for i in range(n):
        #     count = min(count, count_a[i]+b_count)
        #     if s[i] == 'b':
        #         b_count += 1
        
        # return count

        # # time complexity = O(n)
        # # space complexity = O(n)
        

        # n = len(s)
        # count_b = [0]*n
        # count_a = [0]*n
        # b_count = 0
        # for i in range(n):
        #     count_b[i] = b_count
        #     if s[i] == 'b':
        #         b_count += 1
        # a_count = 0
        # for i in range(n-1, -1, -1):
        #     count_a[i] = a_count
        #     if s[i] == 'a':
        #         a_count += 1
        # min_count = n

        # for i in range(n):
        #     min_count = min(min_count, count_b[i]+count_a[i])

        # return min_count

        # # time complexity = O(n)
        # # space complexity = O(n)

        


        