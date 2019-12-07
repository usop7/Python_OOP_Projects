"""
This module defines a simple coroutine that increments a value.
"""

def coroutine_increment():
    """
    This coroutine takes in an increment value and adds it to a running
    total that is yielded. The coroutine should be initially started
    with a call to next that get's the loop going. The coroutine starts
    with a value of 1.
    :return: Yield the total after adding in an increment value that is
    sent in
    """
    i = 0
    increment = 1
    while True:
        i += increment
        increment = yield i


if __name__ == '__main__':
    c1 = coroutine_increment()
    # The first call to next starts the coroutine and gets the loop going.
    print(next(c1))
    total = c1.send(5)
    print(total)
    total = c1.send(47)
    print(total)