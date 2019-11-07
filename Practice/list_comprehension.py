names = ['leesuel', 'christy', 'justin', 'robert', 'eric']
list = [ name for name in names]
print(list)

alphabet_list = [chr(i+65) for i in range(0, 26)]
print(alphabet_list)

even_list = [i for i in range(0, 100) if i % 2 == 0]
print(even_list)

x_list = [i if i % 2 == 0 else 'x' for i in range(0, 100)]
print(x_list)

names = ['leeseul kim', 'justin lee']
first_names = [name.split(' ')[0] for name in names]
print(first_names)