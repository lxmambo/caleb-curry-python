age = 5
stuff = [True, False, 0, -1, "0","10",age < 30, "20","2","5","9001","5.5","6.0",6]

#we want to sort this data as if it's all numbers
stuff.sort(key=float)
print(stuff)

#everytime we have a true is a 1, a false is a 0
#just cannot convert a string to float
#if the list had 'hello' it would give a traceback