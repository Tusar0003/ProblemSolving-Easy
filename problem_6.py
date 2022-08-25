from sys import stdin, stdout


def main():
    n = int(stdin.readline())

    [stdout.write(str(i + 1)) for i in range(n)]


if __name__ == '__main__':
    main()
