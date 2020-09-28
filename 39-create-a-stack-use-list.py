#data structure is a way to store data one way is the stack
#we will use list to create a stack structure

stack = []
stack.append('plate A')
stack.append('plate B')
print(stack.pop())
print(stack)

#my solution to remove a item
favs = []
print("enter a food: ('q' to quit)")
print("if you wanto to remove the last food, type 'pop'")
while True:
    data = input()
    if str.lower(data) == 'q':
        break
    elif str.lower(data) == 'pop':
        favs.pop()
    favs.append(data)
    if str.lower(data) == 'pop':
        favs.pop()
for food in favs:
    print("you said:",food)

#caleb's: use of keyword 'continue'
favs = []
print("enter a food: ('q' to quit)")
print("if you wanto to remove the last food, type 'pop'")
while True:
    data = input()
    if str.lower(data) == 'q':
        break
    elif str.lower(data) == 'pop':
        favs.pop()
        continue
    favs.append(data)
for food in favs:
    print("you said:",food)