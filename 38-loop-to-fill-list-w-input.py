#my code
continue_loop = True
list_of_words = []
while continue_loop:
    word = input("tell me a word: ")
    list_of_words.append(word)
    if word == 'stop':
        continue_loop = False
print(list_of_words)

#caleb's code
favs = []
print("enter a food: ('q' to quit)")
while True:
    data = input()
    if str.lower(data) == 'q':
        break
    favs.append(data)

for food in favs:
    print("you said:",food)