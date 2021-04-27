def TankRush(H1, W1, S1, H2, W2, S2):
    L1 = S1.split()
    L2 = S2.split()
    tmp = []
    if H1 * W1 % H2 * W2 != 0:
        return False

    if (H1 <= 0 or H2 <= 0 or W1 <= 0 or W2 <= 0):
        return False

    if (H2 > H1 or W2 > W1):
        return False

    for i in range(len(L1)):
        for j in range(len(L2)):
            if L2[j] in L1[i]:
                tmp.append(L2[j])
    tmp = set(tmp)
    res = all(item in L2 for item in tmp)
    if res:
        return True
    else:
        return False

#TankRush(5, 15, '000000000000000 000000000000000 000000100000000 000000000000000 000000000000000', 3, 5,'00000 00000 00001')
#print(TankRush(3,3, '321 694 798', 2, 2, '69 98'))