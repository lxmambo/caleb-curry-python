healthy = ["kale chips","broccoli"]
backpack = ["pizza","frozen custard","apple crisp","kale chips"]
backpack2 = ["pizza","frozen custard","apple crisp","kale chips"]


#list comprehension
print(id(backpack))
backpack = [item for item in backpack if item in healthy]
print(backpack)
print(id(backpack))
#->we have 2 different ids. if we are referencing this list
#somewhere else, that connection is going to be lost

print(id(backpack2))
#this is how you slice a list and allows us to replace
# the items in a list without creating a newlist
backpack2[:]=[item for item in backpack2 if item in healthy]
print(backpack2)
print(id(backpack2))
