Fin = open("input.txt")
Fout = open("output.txt", "w+")
n = 0
lst = Fin.readlines()
k = int(lst[0])
members = []
for s in lst[1:]:
    ball = int(s.split()[2])
    if ball > k:
        members.append(s)
members.sort(key="lambda x: x[0]")
Fout.write(str(len(members)) + "\n")
i = 1
for m in members:
    Fout.write(f"{i}) {s[1][0]}. {s[0]}\n")
    i += 1
Fout.close()
