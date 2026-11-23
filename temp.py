w1 = "tail"
w2 = "head"
s = "Bobtail has a tail."
punct = " .,:;!?"
for p in punct:
    s1 = s.replace(' ' + w1 + p, ' ' + w2 + p)
    print(s1)