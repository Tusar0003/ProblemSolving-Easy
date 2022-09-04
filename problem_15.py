def check_palindrome(number):
    temp = int(number)
    rev = 0
    result = ''

    while number > 0:
        dig = number % 10
        rev = rev * 10 + dig
        number = number // 10

    if temp == rev:
        result = True
    else:
        result = False

    return result


if __name__ == '__main__':
    number = int(input().strip())
    print(check_palindrome(number))
