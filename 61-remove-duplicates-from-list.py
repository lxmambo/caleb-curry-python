colors = ['red','red','green','blue','blue', 'blue','blue']
print(set(colors))
print(id(colors))
colors = list(set(colors))
print(colors)
#doing this replaces the variable. if we want to keep
#same are of memory:
print(id(colors))
colors[:] = colors
print(id(colors))

#counting with list comprehension
colors2 = ['red','red','green','blue','blue', 'blue','blue']
count = [[colors2.count(color),color] for color in set(colors2)]
print(count)