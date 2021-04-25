def isSmaller(s1, s2):
    l_s1 = len(s1)
    l_s2 = len(s2)

    if l_s1 < l_s2:
        return True

    if l_s1 > l_s2:
        return False

    for i in range(l_s1):
        if s1[i] < s2[i]:
            return True
        elif s1[i] > s2[i]:
            return False

def BigMinus(s1, s2):
    if isSmaller(s1, s2):
        s1, s2 = s2, s1

    s1_rev = [int(i) for i in s1][::-1]
    s2_rev = [int(i) for i in s2][::-1]

    res = []
    len_small = len(s2_rev)

    for i in range(len_small):
        if s1_rev[i] >= s2_rev[i]:
            res_s = s1_rev[i] - s2_rev[i]
            res.append(res_s)
        else:
            res_s = s1_rev[i] + 10 - s2_rev[i]
            s1_rev[i + 1] = s1_rev[i + 1] - 1
            res.append(res_s)

    for i in range(len(res)):
        s1_rev[i] = res[i]

    s1_rev = s1_rev[::-1]
    return str(int(''.join([str(i) for i in s1_rev])))

#s1 = '1234567890'
#s2 = '1234567890'
#print(BigMinus(s1, s2))
#print(isSmaller(s1, s2))