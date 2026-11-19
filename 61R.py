def primedivisors(n, d=2):
    if n == 1:  # базовый случай: разложение закончено
        return
    if n % d == 0:  # d делит n — это простой сомножитель
        print(d, end=" ")  # печатаем его
        primedivisors(n // d, d)  # продолжаем с оставшейся частью
    else:
        primedivisors(n, d + 1)  # пробуем следующий делитель


N = int(input())
primedivisors(N)
print()
