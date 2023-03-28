

def string_beauty(k, str) -> int:
    max_cnt = 0
    len_str = len(str)
    for a in "abcdefghijklmnopqrstuvwxyz":
        left = 0
        right = 0
        k_left = k
        while 1:
            if right < len_str and (str[right] == a or k_left > 0):
                if str[right] != a:
                    k_left -= 1
                right += 1
            elif left < len_str-1:
                if str[left] != a and left < right:
                    k_left += 1
                left += 1
                right = max(left, right)
            else:
                break
            if right-left > max_cnt:
                max_cnt = right-left
    return max_cnt


if __name__ == '__main__':
    reader = open('input.txt', 'r')
    k = int(reader.readline())
    str = reader.readline().strip()
    reader.close()

    print(string_beauty(k, str))

