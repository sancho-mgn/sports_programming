def MaximumDiscount(N, price):
    price = sorted(price, reverse=True)
    return sum(price[i] for i in range(2, len(price), 3))

# print(MaximumDiscount(7, [100, 350, 500, 250, 200, 50, 400, 435, 23]))
