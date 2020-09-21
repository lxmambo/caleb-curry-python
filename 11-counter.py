from collections import Counter
#counter is a class

backpack = ["sword","rubber duck","slice of pizza","parachute",
"sword", "rubber duck", "slice of pizza", "parachute",
"sword", "rubber duck", "slice of pizza", "parachute",
"sword", "rubber duck", "slice of pizza", "parachute",
"cannon","laser cannon","canon 90D", "can of soup"]

#counter gives us a dictionary and the number
#of occurrencies in the list
print(Counter(backpack))
