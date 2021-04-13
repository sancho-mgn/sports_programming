def PatternUnlock(N, hits):
    result = 0
    for i in range(N - 1):
        next = i + 1
        if (hits[i] == 1 and hits[next] in (6, 2, 9) or
                hits[i] == 2 and hits[next] in (1, 3, 5, 8) or
                hits[i] == 3 and hits[next] in (2, 4, 7) or
                hits[i] == 4 and hits[next] in (3, 5) or
                hits[i] == 5 and hits[next] in (2, 4, 6) or
                hits[i] == 6 and hits[next] in (1, 5) or
                hits[i] == 7 and hits[next] in (3, 8) or
                hits[i] == 8 and hits[next] in (2, 7, 9) or
                hits[i] == 9 and hits[next] in (1, 8)):
            result += 1
        elif (hits[i] == 1 and hits[next] in (5, 8) or
                hits[i] == 2 and hits[next] in (4, 6, 7, 9) or
                hits[i] == 3 and hits[next] in (5, 8) or
                hits[i] == 4 and hits[next] == 2 or
                hits[i] == 5 and hits[next] in (3, 1) or
                hits[i] == 6 and hits[next] == 2 or
                hits[i] == 7 and hits[next] == 2 or
                hits[i] == 8 and hits[next] in (1, 3) or
                hits[i] == 9 and hits[next] == 2):
            result += 2 ** 0.5
    result = str(round(result, 5))
    result = result.replace('0','')
    result = result.replace('.','')
    return result

#N = 3
#hits = [2, 1, 9]
#print(PatternUnlock(N, hits))