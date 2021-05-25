def MatrixTurn(matrix, M, N, T):
    global Matrix
    for i in range(len(matrix)):
        matrix[i] = list(matrix[i])

    if M <= N:
        num_circle = M // 2
    else:
        num_circle = N // 2

    for step in range(T): # количество сдвигов
        tmp = []
        for i in range(num_circle): # количество кругов во круг своей оси
            tmp.append(matrix[i + 1][i])
        for i in range(num_circle):
            horizont_iter = N - i * 2 - 1
            vertic_iter = M - i * 2 - 1
            horizont_iter_circle = N - i - 1
            vertic_iter_circle = M - i - 1

            for a in range(i, horizont_iter + i):
                matrix[i][a], tmp[i] = tmp[i], matrix[i][a]
            for b in range(i, vertic_iter + i):
                matrix[b][horizont_iter_circle], tmp[i] = tmp[i], matrix[b][horizont_iter_circle]
            for c in range(i, horizont_iter + i)[::-1]:
                matrix[vertic_iter_circle][c + 1], tmp[i] = tmp[i], matrix[vertic_iter_circle][c + 1]
            for d in range(i, vertic_iter + i)[::-1]:
                matrix[d + 1][i], tmp[i] = tmp[i], matrix[d + 1][i]

    for j in range(len(matrix)):
        matrix[j] = ''.join(matrix[j])

    Matrix = matrix
    return Matrix

x = MatrixTurn(['123456','234567','345678','456789'], 4,6,1)
print(x)
y = MatrixTurn(["123456", "234567", "345678", "456789"], 4,6, 3)
print(y)

