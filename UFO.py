def con_to_dec(datas, notation):
    res = 0
    datas = str(datas)[::-1]
    for i in range(len(datas)):
        res += int(datas[i]) * notation ** i
    return res


def UFO(N, data, octal):
    res = []
    if octal:
        for i in data:
            notation = 8
            res.append(con_to_dec(i, notation))
        return res
    else:
        for i in data:
            notation = 16
            res.append(con_to_dec(i, notation))
        return res


#N = 2
#data = [1234, 1777]
#octal = False
#print(UFO(N, data, octal))