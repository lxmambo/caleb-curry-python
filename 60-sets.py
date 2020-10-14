items = {"sword","rubber duck", "slice of pizza"}
#a set cannot have duplicates
items.add("sword")
print(items)
#what we want to put in the set must be hashable, lists are not

conjunctions = {"for","and","nor","but","or","yet","so"}
seen = set()
copletely_original_poem = """yet more two more times
i feel nor but or but or, so get me for and 2 or and 
times yet to know but i know you nor i get more for but
"""

data = copletely_original_poem.split()
for word in data:
    if str.lower(word) in conjunctions:
        seen.add(str.lower(word))
print(seen)