from collections import deque


def botva(gamer_1, gamer_2):
    count = 0
    while len(gamer_1) > 0 and len(gamer_2) > 0 and count <= 1000000:
        if gamer_1[0] == 0 and gamer_2[0] == 9:
            gamer_1.append(gamer_1.popleft())
            gamer_1.append(gamer_2.popleft())
        elif gamer_1[0] == 9 and gamer_2[0] == 0:
            gamer_2.append(gamer_1.popleft())
            gamer_2.append(gamer_2.popleft())
        elif gamer_1[0] > gamer_2[0]:
            gamer_1.append(gamer_1.popleft())
            gamer_1.append(gamer_2.popleft())
        elif gamer_2[0] > gamer_1[0]:
            gamer_2.append(gamer_1.popleft())
            gamer_2.append(gamer_2.popleft())
        else:
            return 'botva'
        count += 1

    if len(gamer_1) > 0 and len(gamer_2) == 0:
        return ['first', count]
    elif len(gamer_2) > 0 and len(gamer_1) == 0:
        return ['second', count]
    else:
        return 'botva'


if __name__ == '__main__':
    reader = open('input.txt', 'r')

    line_1 = [*map(int, reader.readline().split())]
    line_2 = [*map(int, reader.readline().split())]

    reader.close()

    gamer_1 = deque(line_1)
    gamer_2 = deque(line_2)

    # print(gamer_1)
    # print(gamer_2)

    for a in botva(gamer_1, gamer_2):
        print(a, end=' ')


