workdays = ["Monday","Tuesday","Thrusday","Friday","Saturday"]
workdays.insert(2,"Wednesday")

del workdays[5]
print(workdays)
del workdays[-1] #grabs the last element
print(workdays)
workdays.append('Friday')
workdays.append('Saturday')
del workdays[workdays.index('Tuesday'):workdays.index('Thrusday')+1]
#slicing/removing from index 1 to index 4 exclusively
print(workdays)