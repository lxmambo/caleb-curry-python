backpack = ["sword","rubber duck","slice of pizza", "parachute","sword"]
print(len(backpack))
print(backpack.count('sword'))

#if "sword" in backpack <=> if backpack.count('sword')>1
if backpack.count('sword')<1:
    backpack.append('sword')
print(backpack)