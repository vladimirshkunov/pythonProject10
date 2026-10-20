from random import randint

n, m = 3, 4
A = []
for _ in range(n):
    row = [randint(1, 10) for _ in range(m)]
    print(*row)
    A.append(row)

maxA = 0
cnt = 0
for i in range(n):
    for j in range(m):
        if A[i][j] > maxA:
            maxA = A[i][j]
            cnt = 1
        elif A[i][j] == maxA:
            cnt += 1
print(maxA, cnt)

B = []
for row in A:
    B += row
print(max(B), B.count(max(B)))
