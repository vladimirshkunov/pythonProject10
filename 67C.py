N, M = map(int, input().split())
A = []
for i in range(N):
    row = [int(x)
           for x in input().split()]
    A.append(row)
K = int(input())
R = int(input())

cnt = 0
for i in range(N):
    for j in range(M):
        if len(str(A[i][j])) == K and \
                sum(map(int, list(str(A[i][j])))) % R == 0:
            cnt += 1

print(cnt)
