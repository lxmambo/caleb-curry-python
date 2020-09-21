healthy = ["kale chips","broccoli"]
backpack = ["pizza","frozen custard","apple crisp","kale chips"]
backpack2 = ["pizza","frozen custard","apple crisp","kale chips"]
backpack3 = ["pizza","frozen custard","apple crisp","kale chips"]


backpack[:] = [item.upper() for item in backpack if item in healthy]
print(backpack)

healthy_backpack = []
for item in backpack2:
    if item in healthy:
        healthy_backpack.append(item.upper())

print(healthy_backpack)

squares = []
for i in range(10):
    squares.append(i**2)
print(squares)

squares = [i**2 for i in range(10)]
print(squares)

squares = [i**2 for i in range(10) if i % 2 == 0]
print(squares)