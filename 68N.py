Fin = open("input.txt")
Fout = open("output.txt", "w+")
lst = Fin.readlines()
w1 = lst[0].strip()
w2 = lst[1].strip()
punct = " .,:;!?\n"
for s in lst[2:]:
    for p in punct:
        s = s.replace(" " + w1 + p, " " + w2 + p)
        s = s.replace(w1.capitalize() + p, w2.capitalize() + p)
    Fout.write(s)
Fout.close()
