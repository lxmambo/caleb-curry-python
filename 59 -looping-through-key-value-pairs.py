emails = {
    'caleb':'caleb@gmail.com',
    'gal':'g@hotmail.com',
    'tim':'timmy@sapo.pt',
}

for key,elem in emails.items():
    print(key,elem)

conjunctions = {
    "for":0,
    "and":0,
    "nor":0,
    "but":0,
    "or":0,
    "yet":0,
    "so":0,
}

copletely_original_poem = """yet more two more times
i feel nor but or but or, so get me for and 2 or and 
times yet to know but i know you nor i get more for but
"""

data = copletely_original_poem.split()
print(data)

for word in data:
    if str.lower(word) in conjunctions:
        conjunctions[str.lower(word)] += 1
print(conjunctions)