from random import randint

a, b, n, k = map(int, input().split())
A = [randint(a, b) for _ in range(n)]
B = [x for x in A if sum(map(int, list(str(x)))) == k]
print(*A)
print(len(B))
