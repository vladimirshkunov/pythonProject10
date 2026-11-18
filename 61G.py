def sumdigits(x):
    if x < 10:
        return x
    else:
        return sumdigits(x // 10) + (x % 10)


n = int(input())
print(sumdigits(n))
