for n in range(2, 100):
    k = 2
    while k * k <= n:
        if n % k == 0: break
        k += 1
    else:
        print(n)
