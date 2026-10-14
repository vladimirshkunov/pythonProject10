from random import randint

a, b, n = map(int, input().split())
A = [randint(a, b) for _ in range(n)]
print(*A)
B = []
C = []
for x in A:
    if x < 50:
        B.append(x)
    else:
        C.append(x)
r1 = sum(B) / len(B) if len(B) else 0
r2 = sum(C) / len(C) if len(C) else 0
print(f'{r1:.3f} {r2:.3f}')
