item1, item2 = (1, 2)
print(item1)
print(item2)


def variable_keyword_args(**kwargs):
    print(kwargs)

    for key, item in kwargs.items():
        print(key, item)


variable_keyword_args(host="localhost", port=21, debug=True)
