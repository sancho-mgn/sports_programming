def squirrel(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return int(str(fact)[0])
print(squirrel(7))