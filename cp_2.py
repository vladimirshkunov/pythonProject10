from evclid import NOD

a, b, c = map(int, input().split())
nod1 = NOD(a, b)
nok1 = a * b // nod1
nod2 = NOD(nod1, c)
nok2 = c * nok1 // nod2
print(nod2, nok2)
