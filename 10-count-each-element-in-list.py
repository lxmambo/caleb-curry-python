backpack = ['sword','rubber duck','slice of pizza','parachute','sword','sword']

count = [backpack.count(item) for item in backpack]
print(count)

#excluding duplicates with count
count = [backpack.count(item) for item in set(backpack)]
print(count)

#generating a list of lists with list comprehension
count = [[backpack.count(item),item] for item in backpack]
print(count)