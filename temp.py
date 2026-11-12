from random import shuffle

A = list(range(1, 16))
shuffle(A)
match int(input("number of group (1 or 2): ")):
    case 1:
        with open("gr1.txt") as f:
            group1 = f.read().split("\n")
        print(list(zip(group1, A)))
    case 2:
        with open("gr2.txt") as f:
            group2 = f.read().strip().split("\n")
        print(list(zip(group2, A)))
