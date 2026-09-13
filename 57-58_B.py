n = int(input())
s = 0
while n:
    s += n
    n -= 1
print(s)

"""
n = int(input())
s = 0
for i in range(1, n+1):
    s += n
print(s)

# ДЛя професионалов:)
print(sum(range(1, int(input())+1)))
"""