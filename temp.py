vowels = 'аеёиоуыэюя'
s = input()
s1 = s[0]
i = 1
cnt = 1
while i < len(s):
    if s[i] in vowels and s[i] == s[i - 1]:
        cnt += 1
    else:
        if cnt == 1:
            s1 += s[i]
        else:
            s1 += str(cnt) + s[i]
            cnt = 1
    i += 1
if cnt > 1:
    s1 += str(cnt)
print(s1)
