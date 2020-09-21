healthy = ["kale chips","broccoli"]
backpack = ["pizza","frozen custard","apple crisp","kale chips",
"pizza slice", "munchicks", "pizza slice", "sandwich from macdonalds"]

backpack.remove("pizza slice")
print(backpack)

while backpack.count('pizza slice') > 0:
    backpack.remove("pizza slice")

print(backpack)