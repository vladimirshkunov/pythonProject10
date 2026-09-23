"""
Напишите программу, которая вводит символьную строку и определяет, какая буква встречается в ней чаще всего.
Если таких букв несколько, можно вывести любую из них.
Пример 1:
Введите строку: ABCABC
Ответ: A
Пример 2:
Введите строку: CBBACAABC
Ответ: C
Пример 3:
Введите строку: BBBBBB
Ответ: B
"""
s = input()
cnt_max = 0
c_max = ''
for c in s:
    if s.count(c) > cnt_max:
        c_max = c
        cnt_max = s.count(c)
print(c_max)

"""
# альтернатива

s=input()
c_tup = [(c, s.count(c)) for c in set(s)]
print(max(c_tup, key=lambda x: c_tup[1])[0])
"""
