data = ["a","b","c","d","e","f","g","h"]

#prints every 2 items
print(data[::2])
#prints reversed
print(data[::-1])

data_reversed = data

data[:] = data[::-1]
print(data)
print(id(data))
print(id(data_reversed))

#doint the slice like this changes only the content of the list
#but doesn't change de list...