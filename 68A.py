Fin = open("input.txt")
Fout = open("output.txt", "w+")

summa = 0
n = 0
for s in Fin:
    summa += int(s)
    n += 1
Fout.write(...)