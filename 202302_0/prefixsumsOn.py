

def countprefixsums(nums):
    prefixsumbyvalue = {0: 1}
    nowsum = 0
    for now in nums:
        nowsum += now
        if nowsum not in prefixsumbyvalue:
            prefixsumbyvalue[nowsum] = 0
        prefixsumbyvalue[nowsum] += 1
    return prefixsumbyvalue


def countzerozsumranges(prefixsumbyvalue):
    cntranges = 0
    for nowsum in prefixsumbyvalue:
        cntsum = prefixsumbyvalue[nowsum]
        cntranges += cntsum * (cntsum - 1) // 2
    return cntranges


if __name__ == '__main__':
    nums = [0, 0, 1, -4, 4, 5, 1, 2, 2, -4]
    prefixsumbyvalue = countprefixsums(nums)
    for key, value in prefixsumbyvalue.items():
        print(key, ": ", value)
    print(countzerozsumranges(prefixsumbyvalue))

