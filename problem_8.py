from collections import OrderedDict

if __name__ == '__main__':
    n = int(input())
    numbers = list(map(int, input().strip().split(' ')))[:n]

    numbers.sort()
    # print(numbers)
    unique_numbers = list(OrderedDict.fromkeys(numbers))
    # print(unique_numbers)
    print(unique_numbers[-2])
