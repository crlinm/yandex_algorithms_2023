from collections import defaultdict
import time


def time_it(func):
    def wrapper(*args, **kwargs):
        print()
        start = time.time()
        print(func.__name__)
        return_value = func(*args, **kwargs)
        end = time.time()
        print('{} sec'.format(end-start))
        return return_value
    return wrapper


# @time_it
def count_simple_dict(string) -> dict:
    d = {}
    for s in string:
        if s not in d:
            d[s] = 0
        d[s] += 1
    return d


# @time_it
def count_set(string):
    max_s = ''
    max_i = 0
    for si in set(string):
        k = 0
        for j in range(len(string)):
            if si == string[j]:
                k += 1
        if k > max_i:
            max_i = k
            max_s = si
    return max_s


# @time_it
def count_defaultdict(string) -> dict:
    d = defaultdict(int)
    for s in string:
        if s != " " and s != '\n' and s != '\r':
            d[s] += 1
    return dict(sorted(d.items()))


def histogram_print(d):
    # print(max(d, key=d.get))
    k_max = max(d.values())
    for i in range(k_max, 0, -1):
        for key, value in d.items():
            print("#", end="") if (i <= value) else print(" ", end="")
        print()

    for key, value in d.items():
        print(key, end="")

    # print()
    # for key, value in d.items():
    #     print(value, end="")


if __name__ == '__main__':
    # s = input()
    s = open("input.txt").read()
    # s = "sssaaqqqqqw"
    # k_max = max(map(lambda x: (s.count(x), x), s))[0]

    # print(lambda x: (s.count(x), x))

    # print(count_set(s))

    histogram_print(count_defaultdict(s))

    # ds = count_simple_dict(s)
    # for key, value in ds.items():
    #     print(key, ": ", value)
