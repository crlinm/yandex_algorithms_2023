from math import ceil


def time_str_to_sec(t):
    tt = int(t[0:2])*60*60 + int(t[3:5])*60 + int(t[6:8])
    return tt


def time_sec_to_str(t):
    h = t//(60*60)
    crt = t-h*(60*60)
    m = (crt)//60
    crt -= m*60
    t_str = '{:02d}:{:02d}:{:02d}'.format(h, m, crt)
    return t_str


def cl_t(tc1_sec, ts_sec, tc2_sec):
    day_sec = 24*60*60
    if tc2_sec < tc1_sec:
        tc2_sec += day_sec
    diff = (tc2_sec - tc1_sec)/2
    diff_round = diff - int(diff)
    if diff_round >= 0.5:
        diff = ceil(diff)
    else:
        diff = int(diff)
    res = ts_sec + diff
    if res > day_sec:
        return res-day_sec
    return res


if __name__ == '__main__':
    reader = open('input.txt', 'r')
    tc1 = reader.readline()
    ts = reader.readline()
    tc2 = reader.readline()
    reader.close()

    # print(tc1, ts, tc2)

    tc1_sec = time_str_to_sec(tc1)
    ts_sec = time_str_to_sec(ts)
    tc2_sec = time_str_to_sec(tc2)

    # print(60*60*24)
    #
    # print(tc1_sec)
    #
    # print(time_sec_to_str(tc1_sec))

    res = cl_t(tc1_sec, ts_sec, tc2_sec)
    # print(res)

    print(time_sec_to_str(res))


