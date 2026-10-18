n = int(input())
A = list(map(int, input().split()))
A.sort(key=lambda x: x % 10)
print(*A)
