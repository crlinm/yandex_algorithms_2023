

def stickers_count(stickers_n, collectors):

    stickers = sorted(list(set(stickers_n)))

    for pi in collectors:

        left = 0
        right = len(stickers)

        while left < right:
            middle = (left + right) // 2
            if stickers[middle] >= pi:
                right = middle
            else:
                left = middle + 1

        print(min(left, len(stickers)))


if __name__ == '__main__':
    reader = open('input.txt', 'r')
    N = int(reader.readline())
    stickers_n = [*map(int, reader.readline().split())]
    K = int(reader.readline())
    collectors_p = [*map(int, reader.readline().split())]
    reader.close()

    stickers_count(stickers_n, collectors_p)

