healthy = ["kale chips","broccoli"]
backpack = ["pizza","frozen custard","apple crisp","kale chips",
"pizza slice", "munchicks", "pizza slice", "sandwich from macdonalds"]

#grabs indexes 3,4 and 5
print(backpack[3:6])
print(backpack[:6])
#way of doing a copy creating a new object pointing to 
#a different space in memory
backpack2 = backpack[:]
print(backpack2)
print(id(backpack))
print(id(backpack2))
print(id(backpack))
backpack[:] = [1,2,3]
print(backpack)
print(id(backpack))
backpack = ['a','b'] #erases data and creates new list, not the same
print(id(backpack))