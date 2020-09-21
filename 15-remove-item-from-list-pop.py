workdays = ["Monday","Tuesday","Thrusday","Friday","Saturday"]
workdays.insert(2,"Wednesday")
print(workdays)

#remove by item
workdays.remove('Saturday')
print(workdays)

#removing by index
del workdays[2]
print(workdays)

#it returns the value in the last index
popped = workdays.pop()
print("we just removed:",popped)

workdays.append('Friday')
workdays.insert(4,'Saturday')
print(workdays)

popped2 = workdays.pop(2)
print(popped2)
print(workdays)
