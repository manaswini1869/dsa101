class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10**9 + 7
        count = 1
        buffer = (n << 1) + 10
        people_knowing = [0] * buffer
        new_people = [0] * buffer
        new_people[1] = 1

        for day in range(1, n+1):
            if new_people[day] > 0:
                people_knowing[day] += new_people[day]

                people_knowing[day + forget] -= new_people[day]

                start = day + delay
                stop = day + forget

                for sharing in range(start, stop):
                    new_people[sharing] += new_people[day]
        MOD = 10**9 + 7
        total = sum(people_knowing[:n+1])
        return total % MOD