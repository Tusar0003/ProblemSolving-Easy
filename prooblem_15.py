def count_substring(string, sub_string):
    count = string.find(sub_string)
    if count < 0:
        count = count + 1
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)

