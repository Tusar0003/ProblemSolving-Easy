if __name__ == '__main__':
    n = int(input())

    # for i in range(0, n):
    #     print('*')

    i = 0
    while i < n:
        i = i + 1
        for j in range(i):
            print('*', end='')
        print('')

    i = n
    while i > 0:
        for j in range(i):
            print('*', end='')
        i = i - 1
        print('')
