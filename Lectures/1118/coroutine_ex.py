def coroutine():
    i = -1
    while i != "exit":
        sign = i / abs(i)
        i = yield (i ** 2) * sign

if __name__ == '__main__':
    c1 = coroutine()
    print(next(c1))
    result = c1.send(-3)
    print(result)
