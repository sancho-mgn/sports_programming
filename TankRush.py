def TankRush(H1, W1, S1, H2, W2, S2):
    L1 = S1.split()
    L2 = S2.split()
    tmp = []
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

#H1 = 3
#W1 = 4
#S1 = '1234 2345 0987'
#H2 = 2
#W2 = 2
#S2 = '34 98'
#print(TankRush(H1, W1, S1, H2, W2, S2))