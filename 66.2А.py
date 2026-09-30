s = input()
cnt_del = 0
while 'B' in s[s.find('R'):]:
    s = s.replace('R', '', 1)
    s = s[::-1]
    s = s.replace('B', '', 1)
    s = s[::-1]
    cnt_del += 2
print(s)
print(cnt_del)
