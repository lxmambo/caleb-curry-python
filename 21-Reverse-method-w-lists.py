data = [0,1,2,3,4,5]
data.reverse()
print(data)
#data.reverse() doesn t returns anything...so
#print(data.reverse()) doesn t print
#when we have a method that doesn't return anything
#we can't use it with print, because print prints what
#is returned
data_copy2 = []
data_copy = data[:]
for i in range(0,len(data)):
    print(data_copy)
    data_copy2.append(data[len(data)-i-1])
 
print(id(data))
print(id(data_copy))
print(data_copy2)