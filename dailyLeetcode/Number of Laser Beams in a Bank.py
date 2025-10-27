class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        m, n = len(bank), len(bank[0])

        num_laser = 0

        security_device = [0]*m

        for i in range(m):
            for j in range(n):
                if bank[i][j] == "1":
                    security_device[i] += 1

        prev = 0
        print(security_device)
        for k in range(len(security_device)):
            if prev < k and security_device[k] != 0:
                num_laser += (security_device[k]*security_device[prev])
                prev = k


        return num_laser