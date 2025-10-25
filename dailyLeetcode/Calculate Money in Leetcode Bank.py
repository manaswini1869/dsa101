class Solution:
    def totalMoney(self, n: int) -> int:

        starter = no_weeks = n // 7
        no_days = n % 7

        total_weeks = 0
        curr_week = 28
        temp_week = 1

        while no_weeks >= 1:
            total_weeks += curr_week
            curr_week += 7
            no_weeks -= 1
            temp_week += 1

        total_days = 0
        for i in range(no_days):
            total_days += temp_week + i

        return total_weeks + total_days

