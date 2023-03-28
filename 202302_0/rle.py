def easypeasy(s):
    def pack(s, cnt):
        if cnt > 1:
            return s + str(cnt)
        else:
            return s

    ans = []
    last_symbol = s[0]
    last_pos = 0
    for i in range(len(s)):
        if s[i] != last_symbol:
            ans.append(pack(last_symbol, i - last_pos))
            last_symbol = s[i]
            last_pos = i
    ans.append(pack(s[i], len(s) - last_pos))
    return ''.join(ans)


if __name__ == '__main__':
    print(easypeasy("sassasdadd"))
