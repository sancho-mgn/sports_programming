def MadMax(N, Tele):
    if N > 1:
        for i in range(N):
            low_index = i
            for j in range(i + 1, N):
                if Tele[j] < Tele[low_index]:
                    low_index = j
            Tele[i], Tele[low_index] = Tele[low_index], Tele[i]
        return Tele[:len(Tele) // 2] + Tele[:len(Tele) // 2 - 1:-1]
    else:
        return Tele

#Tele = [4]
#N = 1
#print(MadMax(N, Tele))