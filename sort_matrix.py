from random import randint

n, m = 3, 4
A = [[randint(1, 10) for _ in range(m)] for _ in range(n)]
B = []
for row in A:
    print(*row)
    B += row
print(max(B), B.count(max(B)))
