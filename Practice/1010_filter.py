num_list = list(range(1, 10))
even_nums_filter = filter(lambda x: x % 2 == 0, num_list)
print(type(even_nums_filter))
print(list(even_nums_filter))

string = "Hello world"
vowels = ['a', 'e', 'i', 'o', 'u']
consonanats = filter(lambda x: x not in vowels, string)
print(list(consonanats))
