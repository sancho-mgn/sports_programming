def odometer(oksana):
    dist = 0
    for j in range(0, len(oksana), 2):
        if j == 0:
            dist += oksana[j] * oksana[j + 1]
        else:
            dist += oksana[j] * (oksana[j + 1] - oksana[j - 1])
    return dist
