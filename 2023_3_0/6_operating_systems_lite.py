def oper_system_lite(M, array):
    if len(array) == 0:
        return 0
    ans = [0 for _ in range(len(array))]
    ans[0] = 1

    for j in range(1, len(array)):
        raz1 = array[j]
        for k in range(0, j):
            raz2 = array[k]
            if raz1[0] <= raz2[1] and raz2[0] <= raz1[1]:
                ans[k] = 0
            ans[j] = 1
    return sum(ans)


if __name__ == '__main__':
    reader = open('input.txt', 'r')
    M = int(reader.readline())
    N = int(reader.readline())
    array = [[] for _ in range(N)]
    for i in range(N):
        array[i] = [*map(int, reader.readline().split())]
    reader.close()

    print(oper_system_lite(M, array))

