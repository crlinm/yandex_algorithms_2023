

def group_words(words):
    groups = {}
    for word in words:
        groups.setdefault(''.join(sorted(word)), []).append(word)
    return groups


if __name__ == '__main__':
    d = group_words(["eat", "tea", "tan", "ate", "nat", "bat"])
    for key, value in d.items():
        print(key, ': ', value)
