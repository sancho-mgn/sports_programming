def squirrel(n):
    fact = 1
    for j in range(1, n + 1):
        fact *= j
    return int(str(fact)[0])
print(squirrel(7))
