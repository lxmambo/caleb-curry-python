print("tell us your favorite veggies")
print("example input(separated by spaces)")
print("kale tomato cucumber broccol")
data = input()
favs = data.split()

for food in favs:
    print("you said:",food)