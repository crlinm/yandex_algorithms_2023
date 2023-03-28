def prefix_matrix_sum(N, M, matrix):
    prefix_matrix_sum = [[0] * M for _ in range(N)]

    first_row_sum = 0
    for j in range(M):
        first_row_sum += matrix[0][j]
        prefix_matrix_sum[0][j] = first_row_sum

    first_clm_sum = 0
    for i in range(N):
        first_clm_sum += matrix[i][0]
        prefix_matrix_sum[i][0] = first_clm_sum

    for i in range(1, N):
        for j in range(1, M):
            prefix_matrix_sum[i][j] = matrix[i][j] + \
                        prefix_matrix_sum[i-1][j] + prefix_matrix_sum[i][j-1] - prefix_matrix_sum[i-1][j-1]
    return prefix_matrix_sum


def rectangle_sum(prefix_matrix_sum, points):
    def get_prefix_sum(i, j):
        return prefix_matrix_sum[i][j] if i >= 0 and j >= 0 else 0
    return get_prefix_sum(points[2] - 1, points[3] - 1) \
        - get_prefix_sum(points[0] - 2, points[3] - 1) \
        - get_prefix_sum(points[2] - 1, points[1] - 2) \
        + get_prefix_sum(points[0] - 2, points[1] - 2)


if __name__ == '__main__':
    points = []
    reader = open('input.txt', 'r')
    N, M, K = map(int, reader.readline().split())
    matrix = [[] for _ in range(N)]
    for i in range(N):
        matrix[i] = [*map(int, reader.readline().split())]
    for i in range(K):
        x1, y1, x2, y2 = [*map(int, reader.readline().split())]
        points.append((x1, y1, x2, y2))
    reader.close()

    prefix_m_sum = prefix_matrix_sum(N, M, matrix)
    # for i in range(N):
    #     print(prefix_m_sum[i])

    for i in range(K):
        print(rectangle_sum(prefix_m_sum, points[i]))

