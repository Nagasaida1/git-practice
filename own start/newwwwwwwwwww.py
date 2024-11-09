n = 5
for i in range(1, n + 1):
    print(' ' * (n - i), end='')
    if i == 1 or i == n:
        print('*' * i)
    else:
        print('*' + ' ' * (i - 2) + '*')
for i in range(n - 1, 0, -1):
    print(' ' * (n - i), end='')
    if i == 1 or i == n:
        print('*' * i)
    else:
        print('*' + ' ' * (i - 2) + '*')
