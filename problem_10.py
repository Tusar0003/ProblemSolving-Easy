def swap_case(input_string):
    chars = list(input_string)

    swap_chars = []
    for c in chars:
        if str(c).isupper():
            swap_chars.append(str(c).lower())
        elif str(c).islower():
            swap_chars.append(str(c).upper())
        else:
            swap_chars.append(c)

    test_string = ''
    return test_string.join(swap_chars)


if __name__ == '__main__':
    s = str(input())
    result = swap_case(s)
    print(result)
