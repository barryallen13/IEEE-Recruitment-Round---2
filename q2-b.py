print('*' * 7)
n = 6
for i in range(5):
    for m in range(n):
        if m == n - 1:
            print('*')
            n -= 1
            break
        else:
            print(' ', end='')
            continue

    i += 1
print('*' * 7)
