def PatternUnlock(N, hits):
    result = 0
    for i in range(N - 1):
        if i == 0:
            if hits[i + 1] - hits[i] == 1:
                result += 1
            else:
                result += 2 ** 0.5
        elif hits[i] - hits[i - 1] == 1:
            result += 1
        else:
            result += 2 ** 0.5
    result = str(round(result, 5))
    result = result.replace('0','')
    result = result.replace('.','')
    return result

#N = 11
#hits = [1, 2, 3, 4, 5, 6, 2, 7, 8, 9, 1]
#print(PatternUnlock(N, hits))