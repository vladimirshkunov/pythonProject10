print('Таблица умножения')
print('   ', end='')
for i in range(1, 10):
    print(f'{i:3.0f}', end='')
print()
print('   ', end='')
for i in range(28):
    print(f'-', end='')
for i in range(1, 10):
    print()
    print(f'{i:2.0f}|', end='')
    for j in range(1, 10):
        print(f'{i * j:3.0f}', end='')
