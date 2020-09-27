data = [1,32,54,34,65,11,100,-1,3]
data_sorted = sorted(data)
#data_final = data_sorted.reverse()
print(data_sorted)
data_sorted.reverse()
data_final = data_sorted[:]
print(data_final)

#another version
print(sorted(data, reverse=True))