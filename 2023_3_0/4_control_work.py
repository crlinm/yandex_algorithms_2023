

def get_place(n, k, row, side):
    place = row * 2 + side
    second_row_1 = -1
    second_row_2 = -1
    if place + k < n:
        second_row_1 = (place + k) // 2
        second_place_1 = (place + k) % 2
    if place - k >= 0:
        second_row_2 = (place - k) // 2
        second_place_2 = (place - k) % 2

    if second_row_1 >= 0:
        if second_row_2 >= 0 and abs(second_row_2 - row) < abs(second_row_1 - row):
            return ' '.join([str(second_row_2 + 1), str(second_place_2 + 1)])
        else:
            return ' '.join([str(second_row_1 + 1), str(second_place_1 + 1)])
    else:
        if second_row_2 >= 0:
            return ' '.join([str(second_row_2 + 1), str(second_place_2 + 1)])
        else:
            return -1


if __name__ == '__main__':
    reader = open('input.txt', 'r')
    N = int(reader.readline())
    K = int(reader.readline())
    row = int(reader.readline())
    side = int(reader.readline())
    reader.close()

    print(get_place(N, K, row-1, side-1))
