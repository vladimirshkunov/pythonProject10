from random import randint, shuffle

n = int(input())
A = [randint(1, n) for _ in range(n)]
print(*A)
shuffle(A)
print(*A)
