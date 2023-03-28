def groupwords(words):
    def keybyword(word):
        symcnt = {}
        for sym in word:
            if sym not in symcnt:
                symcnt[sym] = 0
                symcnt[sym] += 1
        lst = []

        for sym in sorted(symcnt.keys()):
            lst.append(sym)
            lst.append(str(symcnt[sym]))
        return ''.join(lst)

    groups = {}
    for word in words:
        groupkey = keybyword(word)
        if groupkey not in groups:
            groups[groupkey] = []
        groups[groupkey].append(word)
    ans = []
    for groupkey in groups:
        ans.append(groups[groupkey])
    return ans


if __name__ == '__main__':
    # d = groupwords(["eat", "tea", "tan", "ate", "nat", "bat"])
    d = groupwords(["", " _ ", "tan", "ate", "nat", "bat"])
    for ans in d:
        print(ans)
