def TransformTransform(A, N):
    return sum(S(S(A, N), N)) % 2 == 0


def S(A, N):
    B = []
    for i in range(N):
        for j in range(N - i):
            k = i + j
            B.append(max(A[j:k + 1]))
    return B