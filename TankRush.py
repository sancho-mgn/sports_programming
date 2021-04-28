def search(S1, start_str, end_str, start_col, end_col):
    S11 = S1[start_str:end_str]
    for i in range(len(S11)):
        S11[i] = S11[i][start_col:end_col]
    return S11

def TankRush(H1, W1, S1, H2, W2, S2):
    S1 = S1.split()
    S2 = S2.split()

    flag = False
    for i in range((H1 - H2) + 1):
        j = 0
        while j in range(W1):
            start_index = S1[i].find(S2[0], j)
            if start_index != -1:
                end_index = start_index + W2
                end_str = i + H2
                S11 = search(S1, i, end_str, start_index, end_index)
                if S11 == S2:
                    flag = True
                    break
            j += 1
    return flag