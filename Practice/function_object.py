def some_function():
    print("Something")


function_obj = some_function
print(some_function)
print(some_function.__name__)
print(some_function.__class__)
print(type(some_function))
function_obj()