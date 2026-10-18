# bisect не говорит напрямую «есть ли элемент», он даёт индекс вставки,
# чтобы не нарушался порядок
#
# bisect_left и bisect_right для дубликатов
# data_dup = [1, 2, 2, 2, 3]
# print(bisect.bisect_left(data_dup, 2))   # 1 (первый 2)
# print(bisect.bisect_right(data_dup, 2))  # 4 (после всех двоек)

import bisect

n, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
for x in B:
    i = bisect.bisect_left(A, x)
    if i != len(A) and A[i] == x:
        print("YES")
    else:
        print("NO")
