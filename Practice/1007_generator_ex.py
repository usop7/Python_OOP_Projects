def gen_even_multiples(multiplier, start, stop):
    yield from (x * multiplier for x in range(start, stop) if x % 2 == 0)

for result in gen_even_multiples(5, 0, 100):
    print(result)