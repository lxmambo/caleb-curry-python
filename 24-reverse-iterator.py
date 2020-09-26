data = ["a","b","c","d","e","f","g","h"]

data_reversed = []

#nao reverte a lista, faz o iterador ir na outra direcção
for item in reversed(data):
    data_reversed.append(item)

print(data_reversed)