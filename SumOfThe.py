def SumOfThe(N, data):
    for i in data:
        if i == sum(data) - i:
            return i

#data = [5, -25, 10, -35, -45]
#N = len(data)
#print(SumOfThe(N, data))