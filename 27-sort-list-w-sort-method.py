workdays = ["Monday","Tuesday","Thrusday","Friday","Saturday"]
workdays.insert(2,"Wednesday")

workdays_copy = workdays[:] #->copy the content, different address

#sorting alphabetically
workdays.sort()
print(workdays)
print(id(workdays))
print(id(workdays_copy))