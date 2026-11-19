from sys import setrecursionlimit

setrecursionlimit(3000)


def primedevisors(n):
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
