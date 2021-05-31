def Keymaker(k):
    k_list = [0 for _ in range(k)]
    for i in range(k):
        for j in range(k):
            if j % (i + 1) == i:
                    if k_list[j] == 0:
                        k_list[j] = 1
                    else:
                        k_list[j] = 0
    return ''.join(str(i) for i in k_list)