def fibonacci_sequence(n=0):
    current = 0
    prev = 1
    for i in range(n):
        yield current
        prev, current = current, prev + current

for fib_num in fibonacci_sequence(50):
    print(fib_num, end=", ")