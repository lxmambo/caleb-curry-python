#reverse a list manually
data = ["a","b","c","d","e","f","g","h"]

index = 1

#integer division
for index in range(len(data)//2):
    data[index], data[-index-1] = data[-index-1], data[index]

print(data)