l = int(input())
n = int(input())
a = [int(input()) for _ in range(n)]
cnt = 0
i = 0
while i < n:
  if a[i]:
    k = min(l, n - i)
    a[i:i+k] = [0] * (k-1)
    cnt += 1
    i += k - 1
print(cnt)