#join method reverses splip()

data = "this is data"
d = " "
print(data.split(d))

data2 = ['this','is','data']
print(d.join(data2))
d2 = ","
print(d2.join(data2))
print(" ".join(data2))

#if we have numbers in the list we need to str() all elements
data3 = ['this','is','data',5,6]
data4 = []
for element in data3:
    data4.append(str(element))
print(data4)
print(" ".join(data4))

#using comprehension list -> Caleb's version
print(" ".join(str(i) for i in data3))

#using list comprehension without square brakets
#it's knowned has a generator expression