healthy = ["kale chips","broccoli"]
backpack = ["pizza slice","frozen custard","apple crisp","kale chips",
"pizza slice", "munchicks", "pizza slice", "pizza slice","sandwich from macdonalds"]

#this way it's a different ID
print(backpack)
print(id(backpack))
backpack = [item for item in backpack if item !='pizza slice']
print(id(backpack))
print(backpack)

#this way same ID
print(backpack)
print(id(backpack))
backpack[:] = [item for item in backpack if item !='frozen custard']
print(id(backpack))
print(backpack)