healthy = ["kale chips","broccoli"]
backpack = ["pizza","frozen custard","apple crisp","kale chips"]

print(backpack)
backpack.remove("pizza")
print(backpack)

if "frozen custard" not in healthy:
    backpack.remove("frozen custard")

print(backpack)