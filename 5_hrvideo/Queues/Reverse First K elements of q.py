from collections import deque
def reverse_k_elements(q, k):
    temp = []

    for _ in range(k):
        temp.append(q.popleft())

    while temp:
        q.append(temp.pop())

    for _ in range(len(q)-k):
        q.append(q.popleft())

    print(q)



input = input().split()
k = int(input[0])
q = deque([int(x) for x in input[1:]])
reverse_k_elements(q, k)





