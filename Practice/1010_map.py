full_names = [
    "Ross Geller",
    "Rachel Green",
    "Phoebe Buffay",
    "Chandler Bing",
    "Monica Geller",
    "Joey Tribbiani"
]

first_name_map = map(lambda x: x.split()[0], full_names)
print(type(first_name_map))
print(list(first_name_map))

first_names = [x.split()[0] for x in full_names]
last_names = [x.split()[1] for x in full_names]

full_names_map = map(lambda x, y: f"{x} {y}", first_names, last_names)
print(type(full_names_map))
print(tuple(full_names_map))
