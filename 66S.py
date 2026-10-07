s_number = input()
base1, base2 = map(int, input().split())
number = int(s_number, base1)
digits_in_base = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
convert_number = ''
if number < 0:
    sign = '-'
    number = abs(number)
else:
    sign = ''
while number > 0:
    number, remainder = divmod(number, base2)
    convert_number = digits_in_base[remainder] + convert_number
print(sign + convert_number)
