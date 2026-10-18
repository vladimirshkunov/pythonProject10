from random import randint

a, b, n = map(int, input().split())
A = [(randint(a, b), i + 1) for i in range(n)]
print(*[x[0] for x in A])
A.sort()
d = A[1][0] - A[0][0]
id1, id2 = sorted([A[0][1], A[1][1]])
for i in range(2, n):
    if A[i][0] - A[i - 1][0] < d:
        d = A[i][0] - A[i - 1][0]
        id1, id2 = sorted([A[i][1], A[i - 1][1]])
    elif A[i][0] - A[i - 1][0] == d and [id1, id2] < sorted([A[i][1], A[i - 1][1]]):
        id1, id2 = sorted([A[i][1], A[i - 1][1]])
print(*sorted([id1, id2]))
