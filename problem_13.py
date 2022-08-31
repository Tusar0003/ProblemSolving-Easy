def print_full_name(first, last):
    return str('Hello {} {}! You just delved into python.'.format(first, last))


if __name__ == '__main__':
    first_name = str(input())
    last_name = str(input())
    result = print_full_name(first_name, last_name)
    print(result)
