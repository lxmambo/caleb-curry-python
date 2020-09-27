workdays = ["Monday","Tuesday","Thrusday","Friday","Saturday"]
workdays.insert(2,"Wednesday")

#sorted returns a new list and can 
#be used with dictionaries
workdays_sorted = sorted(workdays)
print(workdays_sorted)
print(id(workdays))
print(id(workdays_sorted))
