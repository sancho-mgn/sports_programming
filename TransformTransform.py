def TransformTransform(A, N):
    return sum(S(S(A))) % 2 == 0


def S(A):
    B = []
    for i in range(len(A)):
        for j in range(len(A) - i):
            k = i + j
            B.append(max(A[j:k + 1]))
    return B