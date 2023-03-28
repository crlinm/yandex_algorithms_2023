def easypeasy(s):
    ans = []
    lasts = s[0]
    for i in range(len(s)):
        if s[i] != lasts:
            ans.append(lasts)
            lasts = s[i]
    ans.append(s[i])
    return ''.join(ans)


if __name__ == '__main__':
    print(easypeasy("sassasdadd"))
