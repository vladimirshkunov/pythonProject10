Fin = open("input.txt")
Fout = open("output.txt", "w+")
n = 0
lst = Fin.readlines()
k = int(lst[0])
for s in lst[1:]:
    age = int(s.split()[1])
    if age < k:
        Fout.write(s)
        n += 1
Fout.write(str(n))
Fout.close()
