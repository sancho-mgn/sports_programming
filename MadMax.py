def MadMax(N, Tele):
    for i in range(N):
        low_index = i
        for j in range(i + 1, N):
            if Tele[j] < Tele[low_index]:
                low_index = j
        Tele[i], Tele[low_index] = Tele[low_index], Tele[i]
    return Tele[:len(Tele) // 2] + Tele[:len(Tele) // 2 - 1:-1]

#N = 7
#Tele = [3, 1, 4, 6, 2, 5, 7]
#print(MadMax(N, Tele))