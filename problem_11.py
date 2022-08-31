def split_and_join(s):
    split_string_array = s.split(' ')
    test_string = '-'
    new_string = test_string.join(split_string_array)
    return new_string


if __name__ == '__main__':
    s = input()
    result = split_and_join(s)
    print(result)
