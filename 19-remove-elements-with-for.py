healthy = ["kale chips","broccoli"]
backpack = ["pizza","frozen custard","apple crisp","kale chips",
"pizza slice", "munchicks", "pizza slice", "pizza slice","sandwich from macdonalds"]

for item in backpack:
    if item =='pizza slice':
        backpack.remove(item)

print(backpack)
#you never remove items from a list using a 
#for item.in this case, when we remove an
#item, all the items in front are 
#shifted, if we have 2 pizza slices together
#we remove the first, but the second comes
#to the index of the one we are now...it will
#be skipped

#correct way is to use a copy
for item in backpack[:]:
    if item == "pizza slice":
        backpack.remove(item)

print(backpack)

#another way of doing it:

new_backpack = []
for item in backpack:
    if item !="frozen custard":
        new_backpack.append(item)

backpack = new_backpack
print(backpack)