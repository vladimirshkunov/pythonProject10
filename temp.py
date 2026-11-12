from random import shuffle

group1 = ["Иванов", "Петров", "Сидоров"]
group2 = ["Иван", "Петр", "Сидор"]
A = list(range(1, 16))
shuffle(A)
match int(input('number of group (1 or 2): ')):
    case 1:
        print(list(zip(group1, A)))
    case 2:
        print(list(zip(group2, A)))
