from sys import setrecursionlimit
from functools import lru_cache

setrecursionlimit(100000)


def primedevisors(n):
    @lru_cache(maxsize=None)
    def devisors(x, d=2):
        if x == 1:
            return
        if x % d == 0:  # d делит n — это простой сомножитель
            print(d, end=" ")  # печатаем его
            devisors(x // d, d)  # продолжаем с оставшейся частью
        else:
            devisors(x, d + 1)  # пробуем следующий делитель

    if n == 1:
        print(1)
        return
    else:
        return devisors(n)


n = int(input())
primedevisors(n)

"""
d = 2
while n > 1:
    if n % d == 0:
        print(d, end=" ")
        n //= d
    else:
        d += 1
"""