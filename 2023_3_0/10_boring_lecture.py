def letter_counts(str):
    d = {}
    len_str = len(str)
    for i in range(len_str-1):
        if str[i] not in d:
            d[str[i]] = 0
        d[str[i]] += (i+1) * (len_str-i-1)
    return dict(sorted(d.items()))


if __name__ == '__main__':
    points = []
    reader = open('input.txt', 'r')
    str = reader.readline()
    reader.close()

    d = letter_counts(str)
    for key, value in d.items():
        print('{}: {}'.format(key, value))

