work_days = ['monday','tuesday','thrusday','friday','saturday']
print(work_days)

#insert elemente in a list
work_days.insert(2,'wednesday')
print(work_days)

#remove by value
work_days.remove('saturday')
print(work_days)

#remove by index
del work_days[0]
print(work_days)

#remove with pop
work_days.insert(0,'monday')
work_days.insert(len(work_days),'saturday')
print(work_days)
popped = work_days.pop()
print(work_days)
print("you removed " + popped)
print(f"you removed {popped}")

#using del with slicing
del work_days[0:2] #remove the first 2 (index 2 excluded)
print(work_days)
del work_days[-2:] #remove the last 2
print(work_days)

#remove all occurences in a list
backpack = ["pizza slice","button","pizza slice","fishing pole",
    "pizza slice", "nunchucks","pizza slice","sandwich"]
print(backpack)
backpack.remove("pizza slice") #<-removes one pizza slice
print(backpack)

while(backpack.count("pizza slice") > 0):
    backpack.remove("pizza slice")

print(backpack)

