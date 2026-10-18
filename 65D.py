import bisect

n = int(input())
A = list(map(int, input().split()))
k = int(input())
B = list(map(int, input().split()))
for x in B:
    #    print(A.count(x)) не эффективный линейный поиск
    idL = bisect.bisect_left(A, x)
    if idL != n and A[idL] == x:
        idR = bisect.bisect_right(A, x)
        print(idR - idL)
    else:
        print(0)

