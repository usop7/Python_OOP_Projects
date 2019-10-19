multiple_of_five = lambda x: x*5
print(multiple_of_five(10))

square_root = lambda x: x**(1/2)
list = [1, 2, 3, 4, 5]

result = [square_root(i) for i in list]
print(result)

result2 = [(lambda x: x**0.5)(x) for x in list]
print(result2)