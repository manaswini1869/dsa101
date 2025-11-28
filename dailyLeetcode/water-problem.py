import sys

input = lambda: sys.stdin.readline().rstrip()

N, W = map(int, input().split())
S = []
T = []
P = []

for _ in range(N):
    S_i, T_i, P_i = map(int, input().split())
    S.append(S_i)
    T.append(T_i)
    P.append(P_i)


#The first line contains two integers $N$ and $W$, representing the number of people bathing and the capacity of the water heater.

#The next $N$ lines each contain three integers $S_i$, $T_i$, and $P_i$
# #($0 \le S_i < T_i \le 2 \times 10^5$, $1 \le W, P_i \le 10^9$),
# #representing the bathing plan for the $i$-th person. Here, $S_i$ and $T_i$
# represent the start time and end time of the plan, and $P_i$ represents the amount of hot water required per minute.


timeline = [0] * (2 * 10**5 + 1)
for i in range(N):
    timeline[S[i]] += P[i]
    timeline[T[i]] -= P[i]

print(timeline[:N])

curr = 0
for water in timeline:
    curr += water
    if curr > W:
        print("No")
        sys.exit()

print("Yes")

# for i in range(N):
#     W = W - (T[i] - S[i]) * P[i]
#     if W < 0:
#         print("No")
#         sys.exit()

# print("Yes")