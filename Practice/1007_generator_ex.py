def generate_numbers(upper_bound=0):
    for i in range(upper_bound):
        input("Line before yield")
        yield i
        input("Line after yield")


for result in generate_numbers(9):
    print(result)