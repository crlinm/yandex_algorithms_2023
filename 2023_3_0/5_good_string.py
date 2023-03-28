def string_goodest(array, abc_length):
    sum = 0
    for i in range(abc_length-1):
        sum += min(array[i], array[i+1])
    return sum


if __name__ == '__main__':
    points = []
    reader = open('input.txt', 'r')
    N = int(reader.readline())
    array = [[] for _ in range(N)]
    for i in range(N):
        array[i] = int(reader.readline())
    reader.close()

    print(string_goodest(array, N))
