

if __name__ == '__main__':
    x = []
    y = []
    reader = open('input.txt', 'r')
    N = int(reader.readline())
    for i in range(N):
        xi, yi = [*map(int, reader.readline().split())]
        x.append(xi)
        y.append(yi)
    print(min(x), min(y), max(x), max(y))
    reader.close()
