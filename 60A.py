def min3(a, b, c):
    m = a
    if m > b:
        m = b
    if m > c:
        m = c
    return m


a, b, c = map(int, input().split())
print(min3(a, b, c))
