n = 0
for x in range(51):
    for y in range(51):
        if 3 * x + 2 * y == 100:
            print(x, y)
            n += 1
print(f'{n} решений')
