from sys import stdin, stdout


def main():
    n = int(stdin.readline().strip())

    numbers = []
    for i in range(0, n):
        # a = stdin.readline().strip()
        # numbers.append(a)
        print(i ** 2)

    # [print(i ** 2) for i in range(n)]
    # for number in numbers:
    #     print(int(number) * int(number))
    #     # stdout.write(str(int(number) * int(number)))


if __name__ == '__main__':
    main()
